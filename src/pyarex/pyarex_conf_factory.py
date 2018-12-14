from configparser import ConfigParser, ExtendedInterpolation

import inspect, os

class PyArExConfigFactory:
    """
    Handler for the configuration of PyArEx
    Gets all the appropriate objects from the config file
    Pass them to the parts of code that need them
    """

    def __init__(self,
                 conf_file=None,
                 base_dir=None
                 ):

        if not conf_file:
            raise RuntimeError("Configuration file not provided.")

        if not base_dir:
            base_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

        self.__conf_obj = ConfigParser(interpolation=ExtendedInterpolation())
        self.__conf_obj.read(conf_file)
        self.__base_dir = base_dir

    def get_conf(self, _type):
        return self.__conf_obj[_type]

    def get_conf_path(self):
        return self.__base_dir + '/conf/'

    def get_data_path(self):
        return self.__base_dir + '/data/'

