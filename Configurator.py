from configparser import ConfigParser


class Configurator:
    def __init__(self):
        self.config = ConfigParser()
        self.read_config()

    def read_config(self):
        self.config.read("config.ini")

    def write_config(self):
        with open("config.ini", "w") as config_file:
            self.config.write(config_file)
