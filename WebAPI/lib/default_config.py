import os

from WebAPI.lib.util import JsonDecodeToConfig

default_config = JsonDecodeToConfig(os.getcwd() + r"\WebAPI\conf\configuration.json")
