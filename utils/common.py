import os
import yaml

from .logger import get_logger

LOGGER = get_logger("utils | common")


def read_yml_as_dict(filepath: str) -> dict:
    with open(filepath, "r") as ymlfile:
        output_dict = yaml.safe_load(ymlfile)
    LOGGER.debug("Read yml: %s.", output_dict)
    return output_dict


def save_dict_as_yml(savepath: str, input_dict: dict) -> None:
    with open(savepath, "w") as file:
        yaml.dump(input_dict, file)
    LOGGER.info("Saved config at %s.", savepath)


def check_and_create_dir(directory: str) -> bool:
    exist = os.path.isdir(directory)
    LOGGER.debug("%s exists: %r.", directory, exist)
    if not exist:
        os.mkdir(directory)
        LOGGER.info("%s does not exist, created one.", directory)
    return exist
