import argparse
from config import Config
from logger import setup_logger
from github_client import GitHubClient
from state_manager import StateManager
from processor import RepoProcessor
from summary import Summary

def read_master_repo_list(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    try:
        config = Config()
    except ValueError as e:
        print(e)
        return

    logger = setup_logger(config.LOG_FILE)
    state = StateManager(config.STATE_FILE)
    master_repo_list = read_master_repo_list(config.MASTER_REPO_LIST)
    github_client = GitHubClient(config.GITHUB_TOKEN)
    processor = RepoProcessor(github_client, config.TIME_WINDOW)
    summary = Summary()

    print()
    logger.info("Starting repoCleaner...")
    for repo_name in master_repo_list:
        if repo_name in state.processed_repos:
            print()
            logger.info(f"Skipping already processed repo: {repo_name}")
            continue
        try:
            print()
            logger.info(f"Processing repo: {repo_name}")
            result = processor.process_repo(repo_name)
            summary.add_result(repo_name, result)
            state.add_processed_repo(repo_name)
            logger.info(f"Completed processing repo: {repo_name}")
        except Exception as e:
            print()
            logger.error(f"Error processing repo {repo_name}: {e}")
            break

    summary.generate_report(config.REPORT_FILE)
    print()
    logger.info("Executive summary generated.")
    print()

if __name__ == "__main__":
    main()