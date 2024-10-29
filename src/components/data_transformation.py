import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformerConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class Data_Transformation:
    def __init__(self):
        self.data_transformation_config=DataTransformerConfig()
    
    def get_data_transformer_object(self):
        '''responsible for data transformation'''
        logging.info('Data transformer started')
        try:
            numerical_cols=['writing_score','reading_score']
            categorical_cols=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            num_pipeline=Pipeline(
                steps=[('Imputer',SimpleImputer(strategy='median')),
                        ('Scaler',StandardScaler(with_mean=False))
                ]
            )
            
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                     ('onehot',OneHotEncoder()),
                     ('scaler',StandardScaler(with_mean=False))
                ]
            )
            logging.info(f'numerical columns:{numerical_cols}')
            logging.info(f'categorical columns:{categorical_cols}')

            preprocessor=ColumnTransformer(
                transformers=[
                    ('num_pipeline',num_pipeline,numerical_cols),
                    ('cat_pipeline',cat_pipeline,categorical_cols)
                ]
            )

            return preprocessor



        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info('Reading train and test data completed')
            logging.info('obtaining preprocessing object')
            preprocessor_obj=self.get_data_transformer_object()
            target_column_name="math_score"
            numerical_cols=['reading_score', 'writing_score']
            categorical_cols=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info('applying preprocessing object on training and testing dfs')
            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info('saving preprocessing object')
            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,obj=preprocessor_obj)
            return(
                train_arr,test_arr
            )
        
        except Exception as e:
            raise CustomException(e,sys)
            