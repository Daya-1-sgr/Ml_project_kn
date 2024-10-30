import sys
import os
from dataclasses import dataclass
from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerconfig:
    trained_model_file_path=os.path.join('artfacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerconfig()
    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info('splitting train and test input data')
            X_train,Y_train,X_test,Y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models={
                "Random Forest":RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Gradient Boost":GradientBoostingRegressor(),
                "Linear Regression":LinearRegression(),
                "K Neighbors":KNeighborsRegressor(),
                "Catboost":CatBoostRegressor(verbose=False),
                "Adaboost":AdaBoostRegressor()
            }

            model_report:dict=evaluate_models(x_train=X_train,y_train=Y_train,x_test=X_test,y_test=Y_test,models=models)

            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("No model found with r2 score greater than 0.6")
            logging.info(f"best found model on testing and training dataset is :{best_model_name}")

            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)
            predicted=best_model.predict(X_test)
            r2=r2_score(Y_test,predicted)
            return r2
        except Exception as e:
            raise CustomException(e,sys)

