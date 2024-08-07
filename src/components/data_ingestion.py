import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 
from src.components.data_transformation import DataTransformation



@dataclass
class dataingestionconfig:
    train_data_path : str = os.path.join('artifacts',"train.csv")
    test_data_path : str = os.path.join('artifacts',"test.csv")
    raw_data_path : str = os.path.join('artifacts',"raw.csv")

class dataingestion :
    def __init__(self):
        self.injestion_config = dataingestionconfig()

    def initiate_data_ingestion(self):
        logging.info("Entered Data Ingestion Process")
        try :
            data = pd.read_csv("C:/End to End project/notebook/data/stud.csv")
            logging.info("Loaded the Data")
            
            #we are making folders to store the test , train and raw data
            os.makedirs(os.path.dirname(self.injestion_config.train_data_path),exist_ok=True)
            data.to_csv(self.injestion_config.raw_data_path,index=False,header=True)
            logging.info("train test started :")


            train_set ,test_set = train_test_split(data,test_size=0.2,random_state=1)

            train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of data is done :")

            return(

                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path
                
            )

        except Exception as e :
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = dataingestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)


            



