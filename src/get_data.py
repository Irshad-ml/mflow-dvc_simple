# read the param
# process
# return the dataframe

import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as yaml_files:
        config = yaml.safe_load(yaml_files)
    return config


def get_data(config_path):    
    print(config_path)
    config = read_params(config_path)
    print(config)
    data_path = config["data_source"]["s3_source"]
    print(data_path)
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    return df


# Entry point of this project
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parsed_args=args.parse_args()
    get_data(config_path = parsed_args.config)
    