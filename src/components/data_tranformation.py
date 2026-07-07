##data tranformaton: feature engg+data cleaning
import sys
import pandas as pd
import numpy as np
import os

from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTranformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTranformation:
    def __init__(self):
        self.data_tansformation_config=DataTranformationConfig()
    def get_data_tranformer_object(self):
        try:
            num_columns=[ 'reading_score', 'writing_score']
            cat_columns=['gender',
                        'race_ethnicity', 
                        'parental_level_of_education',
                        'lunch',
                        'test_preparation_course']
            ##creating pipelines for tranformation of data:
            num_pipeline=Pipeline(
                steps=[("imputer",SimpleImputer(strategy='median')),
                       ("scaler",StandardScaler(with_mean=False))])
            cat_pipeline=Pipeline(
                steps=[("imputer",SimpleImputer(strategy='most_frequent')),
                       ("OHE", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
                       ("scaler",StandardScaler(with_mean=False))]
            )
            logging.info('numerical columns standarlized')
            logging.info('categorical columns encoded successfully')
            preprocessor=ColumnTransformer(
                [('num_pipeline',num_pipeline,num_columns),
                 ('cat_pipeline',cat_pipeline,cat_columns)]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def intiate_data_transform(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("imported train_test data")
            logging.info("obtaining preprocessing object")
            preprocesser_obj=self.get_data_tranformer_object()
            target_col_name="math_score"
            num_columns=[ 'reading_score', 'writing_score']
            input_feature_train_df=train_df.drop(target_col_name,axis=1)
            input_feature_test_df=test_df.drop(target_col_name,axis=1)
            target_feature_train_df=train_df[target_col_name]
            target_feature_test_df=test_df[target_col_name]
            logging.info("preprocesser object applied")
            

            input_feature_train_arr=preprocesser_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocesser_obj.transform(input_feature_test_df)
 
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            logging.info('preprocessing completed')

            save_object(file_path=self.data_tansformation_config.preprocessor_obj_file_path,
                        obj=preprocesser_obj)
            return(train_arr,test_arr,self.data_tansformation_config.preprocessor_obj_file_path)
        except Exception as e:
            raise CustomException(e,sys)
    
            

         
