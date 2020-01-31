from os import listdir
from re import match


def get_driver_path(file_name: str):

    def find_driver_by_file_name(file_name):
        def match_file_name(variable):
            return match(file_name, variable)
        return match_file_name

    root_path = "./"

    root_foler_list = listdir(root_path)

    chrome_driver_path = list(
        filter(find_driver_by_file_name(file_name), root_foler_list))

    if len(chrome_driver_path) == 1:
        return root_path + chrome_driver_path[0]
    elif len(chrome_driver_path) == 0:
        raise ValueError(
            'There is no {:s} in project root path.'.format(file_name))
    else:
        raise ValueError(
            'There are more than one {:s} in project root path.'.format(file_name))
