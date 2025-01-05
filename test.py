from utils import get_config


config_file_path = "apiconfig.yaml"
for key, value in get_config(config_file_path).items():
    print(key)