import json
import os

import requests

from utils.config import Config
from utils.singleton import Singleton

GITLAB_HOST = 'https://bj.git.sndu.cn/api/v3'
DEEPIN_NS = 44

class Gitlab(Singleton):
    def __init__(self):
        if hasattr(self, '_init'):
            return

        self._init = True

        c = Config()
        token = c.data('gitlab', 'token')

        self.basic_headers = {
            'PRIVATE-TOKEN': token
        }


    def create_project(self, proj_full_name):
        proj_name = os.path.basename(proj_full_name)

        url = '%s/projects' % GITLAB_HOST
        description = 'mirrored from https://cr.deepin.io/#/admin/projects/%s' % proj_full_name

        d = {
            'name': proj_name,
            'description': description,
            'namespace_id': DEEPIN_NS,
            'visibility_level': 10
        }

        r = requests.post(url, data=d, headers=self.basic_headers)

        return r.status_code, r.text
