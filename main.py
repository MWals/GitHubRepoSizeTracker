# pip install requests
# python script_name.py your_github_username your_github_token

import requests
import argparse


def get_total_disk_usage(username, token):
    total_size = 0
    api_url = f"https://api.github.com/users/{username}/repos"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            total_size += repo['size']
    else:
        print(f"Failed to fetch repositories for user {username}. Status code: {response.status_code}")
    return total_size


def main():
    parser = argparse.ArgumentParser(description='Calculate total disk usage of all GitHub repositories for a user.')
    parser.add_argument('username', type=str, help='GitHub username')
    parser.add_argument('token', type=str, help='GitHub Personal Access Token (PAT)')

    args = parser.parse_args()

    total_size_kb = get_total_disk_usage(args.username, args.token)
    total_size_mb = total_size_kb / 1024
    print(f"Total disk usage for user '{args.username}': {total_size_mb:.2f} MB")


if __name__ == "__main__":
    main()
