import os
from configparser import ConfigParser

from utils.singleton import Singleton

ENV_CONFIG_PATH = os.getenv("CONFIG_PATH")
CONFIG_PATH = ENV_CONFIG_PATH or './config.ini'


class Config(Singleton):

    def __init__(self, path=CONFIG_PATH):
        if hasattr(self, '_init'):
            return

        self._init = True
        self.config = ConfigParser()
        self.config.read(path)

    def data(self, s, n):
        return self.config[s][n]
