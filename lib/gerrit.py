import json

import requests
from requests.auth import HTTPBasicAuth

from utils.config import Config
from utils.singleton import Singleton

GERRIT_HOST = 'https://cr.deepin.io'
GERRIT_MAGIC_JSON_PREFIX = ")]}\'\n"

class Gerrit(Singleton):
    def __init__(self):
        if hasattr(self, '_init'):
            return

        self._init = True

        c = Config()
        self.auth = HTTPBasicAuth(c.data('gerrit', 'username'), c.data('gerrit', 'password'))


    def create_project(self, proj_name, proj_type):
        proj_encode_name = proj_name.replace('/', '%2F')

        if proj_type == 'public':
            parent = 'All-Projects'
        elif proj_type == 'private':
            parent = 'private-project'
        elif proj_type == 'web':
            parent = 'web-projects'
        else:
            print('wrong project type, project type must be one of public, private or web')
            return

        create_empty_commit = True
        url = '%s/a/projects/%s' % (GERRIT_HOST, proj_encode_name)

        d = {
            "parent": parent,
            "create_empty_commit": True
        }

        h = {
            'Content-Type': 'application/json'
        }

        r = requests.put(url, data=json.dumps(d), headers=h, auth=self.auth)
        return r.status_code, r.text
