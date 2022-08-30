import imp
import os 
import pandas as pd
import json

class Extractor:

    def __init__(self):
        pass

    def load_csv(self, path):
        """
        Function to Load csv file.
        """
        df = pd.read_csv(path)
        return df

    def save_df(self,df,filename):
        df.to_csv(filename)
        print("File saved Successfully")

    def read_json(self, json_file: str,dfExtractFunc: object) -> pd.DataFrame:
        """
        json file reader to open and read json files into a panda dataframe
        """
        data_list = []
        for item in open(json_file,'r'):
            data_list.append(json.load(item))

        df = dfExtractFunc(data_list)
        return df

    def read_excel(self,excel_file,startRow = 0) -> pd.DataFrame:
        df = pd.read_excel(excel_file,engine='openpyxl')
        return df