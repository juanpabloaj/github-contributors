#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from git import Repo
import argparse


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


def generate_markdown(author, url):
    return u'[{}]({})'.format(author, url)


def generate_rst(author, url):
    return u'`{} <{}>`_'.format(author, url)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-m', '--markdown', help='Show as markdown', action='store_true'
    )
    parser.add_argument(
        '-r', '--rst', help='Show as rst', action='store_true'
    )

    args = parser.parse_args()

    origin = get_remote()
    contributors = get_contributors_info()
    for author in contributors.keys():
        hash_commit = contributors[author]['hash']
        n_commits = contributors[author]['commits']
        author_url = author_url_from_hash(origin, hash_commit)

        if args.markdown:
            print generate_markdown(author, author_url)
        elif args.rst:
            print generate_rst(author, author_url)
        else:
            print u'{} {} {}'.format(n_commits, author, author_url)


if __name__ == '__main__':
    main()
