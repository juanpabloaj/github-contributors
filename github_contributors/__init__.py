#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from git import Repo


def get_remote(name='origin'):
    repo = Repo()
    remote_url = repo.remotes.origin.url
    return remote_url.split(':')[1].split('.')[0]


def author_url_from_hash(remote, hash_commit):
    github_url = 'https://api.github.com'
    hash_query = '/repos/{}/commits/{}'.format(remote, hash_commit)
    github_query = github_url + hash_query

    req = requests.get(github_query)
    if req.status_code == 200:
        author_github_html_url = req.json()['author']['html_url']
        return author_github_html_url
    return


def get_contributors_info():
    repo = Repo()
    contributors = {}
    for commit in repo.iter_commits('master'):
        author = commit.author
        if author not in contributors.keys():
            hash_commit = commit.hexsha
            contributors[author] = {'commits': 1, 'hash': hash_commit}
        else:
            contributors[author]['commits'] += 1

    return contributors


def main():
    origin = get_remote()
    contributors = get_contributors_info()
    for author in contributors.keys():
        hash_commit = contributors[author]['hash']
        n_commits = contributors[author]['commits']
        author_url = author_url_from_hash(origin, hash_commit)
        print n_commits, author, author_url


if __name__ == '__main__':
    main()
