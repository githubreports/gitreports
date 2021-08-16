import requests
import argparse
import sys
import csv
import time

GITHUB_API = "https://api.github.com"
def cli_parse():
    '''
    :Description: This function takes arguments from command line.
    :return: args
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--organisation', help='organisation', required=True)
    parser.add_argument('--authkey', help='git hub auth key', required=True)
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)
    return args

def get_user_details(headers):
    '''
    :Description: This function makes API calls to get user data in GIT.
    :param headers:
    :return:
    '''
    try:
       user_data = {}
       response_user = requests.get(f"{GITHUB_API}/user", headers=headers)
       user_data["login"] = response_user.json()["login"]
       user_data["name"] = response_user.json()["name"]
       user_data["email"] = response_user.json()["email"]
       return user_data
    except:
        print(sys.exc_info()[0])


def get_all_languages(headers, repo, org):
    '''
    :Description: This function makes API calls to get languages identified in Repo.
    :param headers:
    :param repo_list:
    :param login:
    :return:
    '''
    try:
       response_lang = requests.get(f"{GITHUB_API}/repos/{org}/{repo}/languages", headers=headers)
       return [*response_lang.json()]
    except:
        print(sys.exc_info()[0])

def github_apicall(args):
    '''
    :Description: This Function makes calls to github API.
    :param args:
    :return:
    '''
    repo_list = []
    lang_list = []
    org = args.organisation
    key = args.authkey
    headers = {'Authorization': 'token ' + key, 'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36')}
    try:
       rate_limit = requests.get(f"{GITHUB_API}/rate_limit", headers=headers)
       print(rate_limit.json())
       user_data = get_user_details(headers)
       response_repos = requests.get(f"{GITHUB_API}/orgs/{org}/repos", headers=headers)
       for repo in response_repos.json():
           repo_list.append(repo["name"])
       repo_list = list(set(repo_list))
       print(repo_list)
       for repo in repo_list:
           languages = get_all_languages(headers, repo, org)
           lang_list.extend(languages)
       lang_list = list(set(lang_list))
       user_data["repos"] = ",".join(repo_list)
       user_data["languages"] = ",".join(lang_list)
       generate_csv_report(user_data)
    except:
       print(sys.exc_info()[0])


def generate_csv_report(data):
    '''
    :Description : This function takes dictionary as input and writes to a csv file.
    :param data:
    :return:
    '''
    try:
       with open(data["name"]+".csv", 'w') as csvfile:
           w = csv.DictWriter(csvfile, delimiter=';', fieldnames=data.keys())
           w.writeheader()
           w.writerow(data)
    except:
       print(sys.exc_info()[0])

if __name__ == "__main__":
    fields = ['Login', 'Name', 'Email', 'Repos', 'Languages']
    args = cli_parse()
    github_apicall(args)