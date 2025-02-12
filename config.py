import os
from datetime import timedelta

class Config:
    def __init__(self):
        self.GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
        if not self.GITHUB_TOKEN:
            self.GITHUB_TOKEN = input("\nEnter your GitHub Token: ").strip()
        
        self.MASTER_REPO_LIST = 'masterRepoList.txt'
        
        # Convert user input to timedelta
        default_stale_days = 365
        user_input = input(f"Enter stale branch threshold (days, default {default_stale_days}): ").strip()
        try:
            stale_days = int(user_input) if user_input else default_stale_days
        except ValueError:
            stale_days = default_stale_days
            
        self.TIME_WINDOW = timedelta(days=stale_days)  # Convert to timedelta
        
        self.STATE_FILE = '.repocleaner_state.json'
        self.REPORT_FILE = 'executive_summary.md'
        self.LOG_FILE = 'repocleaner.log'