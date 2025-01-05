import yaml 

def get_config(filePath):
    with open(filePath, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config['parameters']