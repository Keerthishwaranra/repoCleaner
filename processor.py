from datetime import datetime, timezone
import logging

# Initialize logger
logger = logging.getLogger('repoCleaner')

class RepoProcessor:
    def __init__(self, github_client, time_window):
        self.github_client = github_client
        self.time_window = time_window

    def _get_user_selection(self, stale_branches, repo_name):
        print(f"\nStale branches in {repo_name}:")
        for idx, branch in enumerate(stale_branches, 1):
            print(f"{idx}. {branch['name']} (last commit: {branch['commit_date'].strftime('%Y-%m-%d')})")
        while True:
            choice = input("Enter branch numbers to delete (comma-separated, 'a' for all, 'n' for none): ").strip()
            if choice.lower() == 'a':
                return [b['name'] for b in stale_branches]
            elif choice.lower() == 'n':
                return []
            else:
                try:
                    indices = [int(i.strip()) - 1 for i in choice.split(',')]
                    selected = [stale_branches[i]['name'] for i in indices]
                    return selected
                except (ValueError, IndexError):
                    print("Invalid input. Please try again.")

    def process_repo(self, repo_name):
        repo = self.github_client.get_repo(repo_name)
        default_branch = repo.default_branch
        branches = self.github_client.get_branches(repo)
        branch_data = []
        for branch in branches:
            commit_date = branch.commit.commit.author.date
            now_utc = datetime.now(timezone.utc)
            is_stale = (now_utc - commit_date) > self.time_window
            branch_data.append({
                'name': branch.name,
                'stale': is_stale,
                'commit_date': commit_date,
                'is_default': branch.name == default_branch
            })
        stale_non_default = [b for b in branch_data if b['stale'] and not b['is_default']]
        deleted_branches = []
        if stale_non_default:
            selected_branches = self._get_user_selection(stale_non_default, repo_name)
            for branch_name in selected_branches:
                try:
                    self.github_client.delete_branch(repo, branch_name)
                    deleted_branches.append(branch_name)
                except Exception as e:
                    print(f"Failed to delete branch {branch_name}: {e}")
        else:
            logger.info(f"No stale branches found in {repo_name}")
        remaining_branches = [b for b in branch_data if b['name'] not in deleted_branches and not b['is_default']]
        all_remaining_stale = all(b['stale'] for b in remaining_branches)
        all_branches_stale = all(b['stale'] for b in branch_data)
        return {
            'stale_branches': len(stale_non_default),
            'deleted': deleted_branches,
            'recommend_delete_repo': all_remaining_stale and all_branches_stale
        }