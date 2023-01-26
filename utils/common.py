import logging
import os
import yaml


def getLogger(logger_name: str) -> logging.Logger:
    format = "%(asctime)s [%(name)s | %(levelname)s]: %(message)s"
    datefmt = '%Y-%m-%d %H:%M:%S'
    logger = logging.getLogger(logger_name)
    level = int(os.getenv("LOGGER_LEVEL"))
    logging.basicConfig(level=level, format=format, datefmt=datefmt)
    logger.debug(f"Logger started, level={level}")
    return logger

LOGGER = getLogger("Common")


def readYmlAsDict(ymlPath:str) -> dict:
    LOGGER.info(f"Reading {ymlPath=}")
    with open(ymlPath, "r") as ymlFile:
        data = yaml.load(ymlFile, Loader=yaml.SafeLoader)
    LOGGER.debug(f"Dict content: {data}")
    return data


def saveDictAsYml(savePath:str, saveDict:dict) -> None:
    LOGGER.debug(f"Saving dict: {saveDict}")
    with open(savePath, 'w') as file:
        yaml.dump(saveDict, file)
    LOGGER.info(f"Saved config at {savePath}")


def checkAndCreateDir(directory:str) -> bool:
    exist = os.path.isdir(directory)
    LOGGER.debug(f"{directory} exists: {exist}")
    if not exist:
        LOGGER.info(f"{directory} does not exist, creating one.")
        os.mkdir(directory)
    return exist
