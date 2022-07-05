import os 
import yaml
import pandas as pd
import argparse
from get_data import read_params,get_data



def load_and_save(config_path):
    print("hello")
    config=read_params(config_path)
    df=get_data(config_path)
    print(df.head())
    #replace the blank space between column names
    new_cols= [col.replace(" ","_") for col in df.columns]
    raw_data_path=config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path,index=False,sep=",",header=new_cols)
    



#Entry point of this project
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    load_and_save(config_path = parsed_args.config)