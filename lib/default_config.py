import os

from lib.util import JsonDecodeToConfig

default_config = JsonDecodeToConfig(os.getcwd() + r"\conf\configuration.json")
