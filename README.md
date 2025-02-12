# 🧹 repoCleaner - GitHub Stale Repo/Branch Cleaner 🧙♂️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/Keerthishwaranra/repoCleaner)](https://github.com/yourusername/repoCleaner/issues)

A smart utility to identify and clean stale GitHub repositories/branches with surgical precision! 🔍🗑️

## 🌟 Features
- ✅ **Stale Branch Detection** (1+ year old commits)
- 📄 **Repo List Management** via `masterRepoList.txt`
- 🛡️ **Safe Deletion** with user confirmation
- 📊 **Executive Summary** generation
- 🔄 **Network Recovery** from interruptions
- 🚨 **Protection** against accidental deletions
- 📝 **Detailed Logging** for audit trails

## 🚀 Getting Started

### 📥 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repoCleaner.git
   cd repoCleaner
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
   
3. Activate the virtual environment:

    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    venv\Scripts\activate
    ```
   
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
6. Deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

 ### ⚙️ Configuration
1. Create .env file:
   ```bash
   echo "GITHUB_TOKEN=your_personal_access_token_here" > .env
   ```
2. Create and populate masterRepoList.txt:
    Create the file:
    ```bash
    touch masterRepoList.txt
   ```
    Add repositories to clean (one per line):
    ```bash
    yourusername/repo1
    yourusername/repo2
    yourusername/repo3
    yourusername/repo4
   ```
    Example:
    ```bash
    Keerthishwaranra/docs
    Keerthishwaranra/gh-ost
    Keerthishwaranra/dmca
    Keerthishwaranra/DPG-guidance
    ```


###  🛠️ Usage
```bash
python3 main.py
```

###  💻 Sample Output
```
🕒 2025-02-13 02:46:38,988 - Processing repo: Keerthishwaranra/gh-ost
✅ No stale branches found in Keerthishwaranra/gh-ost
🗑️ Deleted 2 stale branches from Keerthishwaranra/docs
📄 Report generated: executive_summary.md
```

### 📊 Executive Summary Example
```
# 📑 Executive Summary
## 📦 Repository: Keerthishwaranra/docs
- 🗑️ Deleted branches:
  🪶 old-feature-branch
  🪶 experimental-changes
- 🚨 Recommendation: Consider deleting repository (all branches stale)

## 📈 Statistics
🔄 Processed repositories: 4
⏳ Stale repositories: 1
🗑️ Total branches deleted: 2
```

### 🔄 Network Recovery
Automatically resumes from last successful operation using:

```
// .repocleaner_state.json
{
  "processed_repos": ["repo1", "repo2"]
}
```

### 🤝 Contributing
1.🍴 Fork the repository

2.🌿 Create your feature branch

3.💾 Commit changes

4.🚀 Push to the branch

5.🔀 Open a Pull Request

### 📜 License
MIT © [Keerthishwaran R A] - See [LICENSE](https://github.com/Keerthishwaranra/repoCleaner/blob/main/LICENSE) for details

### 💬 Support
Found a bug? 🐛

Need help? ❓

Feature request? ✨

[Open an Issue](https://github.com/Keerthishwaranra/repoCleaner/issues/new)

