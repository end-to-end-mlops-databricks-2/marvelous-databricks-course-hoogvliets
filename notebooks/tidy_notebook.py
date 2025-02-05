# Databricks notebook source
from loguru import logging

import yaml

from src.powercons.config import ProjectConfig
from src.powercons.preprocessing import Preprocessor

config = ProjectConfig.from_yaml("config/config.yaml")
logger.info("Config loaded successfully")
logger.info(config, default_flow_style=False)


# COMMAND ----------

# Load the data
# TODO replace with loading from Databricks volume

!bash ../scripts/download_data.sh

# COMMAND ----------

# Initialize the preprocessor
data_preprocessor = Preprocessor(df, config)

# Preprocess the data
data_preprocessor.preprocess()

# COMMAND ----------

# Split data into test, train and validation sets
train_df, test_df, val_df = data_preprocessor.split_data()

# COMMAND ----------


