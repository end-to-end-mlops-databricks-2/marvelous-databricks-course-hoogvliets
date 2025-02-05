# Databricks notebook source
# MAGIC %pip install kagglehub

# COMMAND ----------

import kagglehub
import pandas as pd
import os
from pandas import DataFrame

def get_data_from_kaggle(kaggle_path: str) -> DataFrame:
    path = kagglehub.dataset_download(kaggle_path)
    df = pd.read_csv(os.path.join(path))
    return df

# COMMAND ----------


