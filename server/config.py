import toml

def parse_config_file(env):
    config_file = "/conf/{}/config.toml".format(env)

    with open(config_file, "r") as file:
        config = toml.load(file)
    return config
