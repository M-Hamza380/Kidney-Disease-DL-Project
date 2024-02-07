import sys

from src.classifier.config.configuration import ConfigurationManager
from src.classifier.components.data_ingestion import DataIngestion
from src.classifier.exception import CustomException
from src.classifier.logger import logging

Stage_Name = 'Data Ingestion Stage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config= data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logging.info(f"stage {Stage_Name} started")
        obj =  DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f"stage {Stage_Name} completed")
    except Exception as e:
        logging.info(e)
        raise CustomException(e, sys)

