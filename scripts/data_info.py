# import 
import pandas as pd

class DataInfo:
    def __init__(self, df):
        self.df = df.copy()

    # shape of the dataframe
    def shape_df(self):
         '''
         Display number of rows and columns in the given Dataframe
         '''
         print(f"Dataframe contains {self.df.shape[0]} rows and {self.df.shape[1]} columns")
         #return (self.df.shape[0],self.df.shape[1])
    # info
    def detail_info(self):
        '''
        Display detail Dataframe info
        '''
        print(self.df.info())
    # satistical description
    def describe_stat(self):
        '''
        Display the statistical description of the given dataframe
        '''
        return self.df.describe()
    # null percentage 
    def null_percentage(self):
        '''
        Display Total Null percentage of the Data Frame
        '''
        number_of_rows, number_of_columns = self.df.shape
        df_size = number_of_rows * number_of_columns
        null_size = (self.df.isnull().sum()).sum()
        percentage = round((null_size / df_size) * 100, 2)
        print(f"Dataframe contains null values of { percentage }% out of the given dataset")
    # counts null
    def get_count_null(self):
        print(self.df.isnull().sum())
    
    # duplication
    def get_duplication(self):
        print(self.duplicated().sum())
        
    # datatyps
    def get_tyep(self):
        print(self.dtype)



