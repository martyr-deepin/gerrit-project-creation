#!/usr/bin/python3

import os
import argparse

from lib.gerrit import Gerrit
from lib.gitlab import Gitlab
from lib.github import Github


def new_project(proj_name, proj_type):
    g = Gerrit()
    print('\n--- gerrit ---')
    code, msg = g.create_project(proj_name, proj_type)

    if not str(code).startswith('2'):
        print(msg)
        print('E: failed')

    print('finish gerrit')

    # github
    print('\n--- github ---')
    gh = Github()
    code, msg = gh.create_project(proj_name)

    if not str(code).startswith('2'):
        print(msg)
        print('E: failed')

    print('finish github')

    # gitlab
    print('\n--- gitlab ---')
    gl = Gitlab()
    code, msg = gl.create_project(proj_name)

    if not str(code).startswith('2'):
        print(msg)
        print('E: failed')

    print('finish gitlab')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='project name')
    parser.add_argument('-t', '--type', help='project type [public | private | web]')
    args = parser.parse_args()
    proj_name = args.name
    proj_type = args.type

    new_project(proj_name, proj_type)
