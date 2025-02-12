from datetime import datetime
import logging

logger = logging.getLogger('repoCleaner')

class Summary:
    def __init__(self):
        self.results = []

    def add_result(self, repo_name, result):
        self.results.append({
            'repo': repo_name,
            'deleted': result['deleted'],
            'recommend_delete_repo': result['recommend_delete_repo']
        })

    def generate_report(self, filename):
        report_content = [
            "# Executive Summary",
            f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        ]

        total_deleted = 0
        total_repos = len(self.results)
        repos_with_stale = 0

        for res in self.results:
            repo_section = [
                f"## Repository: {res['repo']}",
                f"- Branches deleted: {len(res['deleted'])}" if res['deleted'] else "- No stale branches found"
            ]

            if res['deleted']:
                repo_section.append("  - " + "\n  - ".join(res['deleted']))
                total_deleted += len(res['deleted'])
                repos_with_stale += 1

            if res['recommend_delete_repo']:
                repo_section.append("- **Recommendation**: Delete this repository as all remaining branches are stale")

            report_content.append("\n".join(repo_section))

        # Add summary statistics
        summary_stats = [
            "\n## Summary Statistics",
            f"- Total repositories processed: {total_repos}",
            f"- Repositories with stale branches: {repos_with_stale}",
            f"- Total branches deleted: {total_deleted}"
        ]
        report_content.extend(summary_stats)

        # Save to file
        with open(filename, 'w') as f:
            f.write("\n\n".join(report_content))

        # Print console version
        console_output = "\n".join([
            "\nExecutive Summary:",
            f"Total repositories processed: {total_repos}",
            f"Repositories with stale branches: {repos_with_stale}",
            f"Total branches deleted: {total_deleted}",
            "\nDetailed results saved to: " + filename
        ])
        print(console_output)