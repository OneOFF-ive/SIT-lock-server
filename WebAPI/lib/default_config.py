import os

from WebAPI.lib.util import JsonDecodeToConfig

default_config = JsonDecodeToConfig(os.getcwd() + r"\conf\configuration.json")
