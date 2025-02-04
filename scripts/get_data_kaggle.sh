#!/bin/bash

# download the dataset
curl -L -o ~/Downloads/power-consumption.zip\
  https://www.kaggle.com/api/v1/datasets/download/nayanack/power-consumption

# create data directory if it doesn't exist
mkdir -p ./data

# move and unzip the file
mv ~/Downloads/power-consumption.zip ./data/
cd ./data
unzip power-consumption.zip

# remove the zip file
rm power-consumption.zip

# rename file
mv "Tetuan City power consumption.csv" "tcpc_kaggle.csv"
