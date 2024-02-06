# GitHub Repository Size Tracker

## Overview
The GitHub Repository Size Tracker is a simple yet powerful Python script that calculates the total disk usage of your GitHub repositories. It allows users to specify the scope of repositories to include in the calculation: all, public, or private.

## Prerequisites
Before you begin, ensure you have the following:
- A GitHub Personal Access Token with the `repo` scope. Create one [here](https://github.com/settings/tokens).
- Python installed on your system.
- The `requests` library installed. You can install it using pip:

```bash
pip install requests
```

## Usage
To use the script, run the following command in your terminal:

```bash
python main.py <your_github_username> <your_github_token> <repo_scope>
```

Replace `<your_github_username>` with your GitHub username, `<your_github_token>` with your GitHub Personal Access Token, and `<repo_scope>` with `all`, `public`, or `private` depending on the repositories you want to include in the calculation.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
