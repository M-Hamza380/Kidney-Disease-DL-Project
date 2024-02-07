import sys

from src.classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.classifier.logger import logging
from src.classifier.exception import CustomException

Stage_Name = 'Data Ingestion Stage'
try:
    logging.info(f'stage {Stage_Name} has started')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f'stage {Stage_Name} has completed')

except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)

