from pandas import DataFrame, to_datetime, to_numeric
from sklearn.model_selection import train_test_split

from src.powercons.config import ProjectConfig


class Preprocessor:
    """
    Preprocesses the data according to the configuration.
    """

    def __init__(self, config: ProjectConfig, df: DataFrame):
        self.config = config
        self.df = df

    def preprocess_data(self):
        # Set the datatypes of the numerical features
        for col in self.config.numerical_features:
            self.df[col] = to_numeric(self.df[col], errors="coerce")

        # Set the datatypes of the timestamps
        for col in self.config.timestamps:
            self.df[col] = to_datetime(self.df[col])

        # Set the datatypes of the targets
        for col in self.config.targets:
            self.df[col] = to_numeric(self.df[col], errors="coerce")

        # Aggregate targets
        self.df["target"] = self.df[self.config.targets].sum(axis=1)

        # Organise columns
        self.df = self.df[self.config.numerical_features]
        self.df["timestamp"] = self.df[self.config.timestamp]

    def split_data(self, test_size: float, random_state: int) -> tuple[DataFrame, DataFrame, DataFrame]:
        train_df, test_df = train_test_split(
            self.df, test_size=self.config.train_params.test_size, random_state=self.config.train_params.random_state
        )
        test_df, val_df = train_test_split(
            test_df, test_size=self.config.train_params.val_size, random_state=self.config.train_params.random_state
        )
        return train_df, test_df, val_df
