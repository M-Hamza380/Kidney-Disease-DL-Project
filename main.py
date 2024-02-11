import sys

from src.classifier.logger import logging
from src.classifier.exception import CustomException
from src.classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.classifier.pipeline.stage_03_model_training import ModelTrainingPipeline


Stage_Name = 'Data Ingestion Stage'

try:
    logging.info('*'*20)
    logging.info(f'stage {Stage_Name} has started')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f'stage {Stage_Name} has completed')

except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)


Stage_Name = 'Prepare Base Model'

try:
    logging.info('*'*20)
    logging.info(f'stage {Stage_Name} has started')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f'stage {Stage_Name} has completed')

except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)


Stage_Name = 'Model Training'

try:
    logging.info('*'*20)
    logging.info(f'stage {Stage_Name} has started')
    prepare_base_model = ModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f'stage {Stage_Name} has completed')

except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)

