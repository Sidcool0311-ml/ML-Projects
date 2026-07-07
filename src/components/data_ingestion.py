import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_tranformation import DataTranformation, DataTranformationConfig


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def intiate_data_ingestion(self):
        logging.info("enter data ingestion component")
        try:
            df=pd.read_csv("notebook/stud.csv")
            logging.info("exported dataset")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('train_test intiated')
        
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("ingestion completed")
            return(
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.intiate_data_ingestion()
    
    data_tranformation=DataTranformation()
    train_data,test_data,_= data_tranformation.intiate_data_transform(train_data,test_data)

    