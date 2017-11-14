import json
import os

import requests

from utils.config import Config
from utils.singleton import Singleton

GITHUB_HOST = 'https://api.github.com'

class Github(Singleton):
    def __init__(self):
        if hasattr(self, '_init'):
            return

        self._init = True

        c = Config()
        token = c.data('github', 'token')

        self.basic_headers = {
            'Authorization': 'token %s' % token,
            'Content-Type': 'application/json'
        }


    def create_project(self, proj_full_name):
        proj_name = os.path.basename(proj_full_name)

        url = '%s/orgs/linuxdeepin/repos' % GITHUB_HOST
        description = 'mirrored from https://cr.deepin.io/#/admin/projects/%s' % proj_full_name

        d = {
            "name": proj_name,
            "description": description
        }

        r = requests.post(url, data=json.dumps(d), headers=self.basic_headers)

        if not str(r.status_code).startswith('2'):
            # not normal
            return r.status_code, r.text

        print('finish creation')
        print('granting deepin-gerrit push permission')

        status_code, text = self.grant_permission(proj_name)

        return status_code, text


    def grant_permission(self, proj_name):
        replication_user = 'deepin-gerrit'
        url = '%s/repos/linuxdeepin/%s/collaborators/%s' % (GITHUB_HOST, proj_name, replication_user)
        permission = 'push'

        d = {
            "permission": permission
        }

        r = requests.put(url, data=json.dumps(d), headers=self.basic_headers)
        print('+++++++++++')
        print(r.json())
        print('+++++++++++')
        return r.status_code, r.text
