from pathlib import Path

from loguru import logger
from pandas import DataFrame, read_csv


def load_data(path: str) -> DataFrame:
    logger.info("Path to dataset file: %s", path)
    df = read_csv(Path(".") / path)
    return df
