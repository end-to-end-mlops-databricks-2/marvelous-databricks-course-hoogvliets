from pandas import DataFrame, read_csv
from loguru import logger
from pathlib import Path

def load_data(path: str) -> DataFrame:
    logger.info("Path to dataset file: %s", path)
    df = read_csv(Path(".")/path)
    return df


