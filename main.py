#!/usr/bin/python3

import os
import argparse

from lib.gerrit import Gerrit
from lib.gitlab import Gitlab
from lib.github import Github


def new_project(proj_name, proj_type, git_target):

    git_targets = git_target.split(',')

    if 'gerrit' in git_targets:
        g = Gerrit()
        print('\n--- gerrit ---')
        code, msg = g.create_project(proj_name, proj_type)

        if not str(code).startswith('2'):
            print(msg)
            print('E: failed')

        print('finish gerrit')

    if 'github' in git_targets and proj_type == 'public':
        print('\n--- github ---')
        gh = Github()
        code, msg = gh.create_project(proj_name)

        if not str(code).startswith('2'):
            print(msg)
            print('E: failed')

        print('finish github')

    if 'gitlab' in git_targets:
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
    parser.add_argument('-g', '--git', help='choose one or multi target, [gerrit | github | gitlab], eg: github,gitlab')
    args = parser.parse_args()
    proj_name = args.name
    proj_type = args.type
    git = args.git

    new_project(proj_name, proj_type, git)
