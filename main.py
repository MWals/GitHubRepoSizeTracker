import requests
import argparse

def get_repo_sizes(username, token, visibility):
    total_size = 0
    page = 1
    while True:
        api_url = f"https://api.github.com/users/{username}/repos?type={visibility}&per_page=100&page={page}"  # Added 'type=all' to include every type of repo
        headers = {'Authorization': f'token {token}'}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            repos = response.json()
            if not repos:
                break  # Break the loop if no more repositories
            for repo in repos:
                name = repo['name']
                size_kb = repo['size']
                size_mb = size_kb / 1024
                total_size += size_kb
                print(f"Repo: {name}, Size: {size_mb:.2f} MB")
            page += 1  # Proceed to next page
        else:
            print(f"Failed to fetch repositories for user {username}. Status code: {response.status_code}")
            break

    return total_size

def main():
    parser = argparse.ArgumentParser(description='List GitHub repositories for a user and their sizes, including private ones, with a total sum.')
    parser.add_argument('username', type=str, help='GitHub username')
    parser.add_argument('token', type=str, help='GitHub Personal Access Token (PAT) with `repo` scope')
    parser.add_argument('visibility', type=str, help='Type of repo, all, public or private')

    args = parser.parse_args()

    total_size_kb = get_repo_sizes(args.username, args.token, args.visibility)
    total_size_mb = total_size_kb / 1024
    print(f"Total disk usage of {args.visibility} repos of user '{args.username}': {total_size_mb:.2f} MB")

if __name__ == "__main__":
    main()

