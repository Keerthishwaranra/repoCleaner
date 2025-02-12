import json
import os

class StateManager:
    def __init__(self, state_file):
        self.state_file = state_file
        self.processed_repos = []
        self.load()

    def load(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                data = json.load(f)
                self.processed_repos = data.get('processed_repos', [])

    def add_processed_repo(self, repo_name):
        if repo_name not in self.processed_repos:
            self.processed_repos.append(repo_name)
            self.save()

    def save(self):
        data = {'processed_repos': self.processed_repos}
        with open(self.state_file, 'w') as f:
            json.dump(data, f)