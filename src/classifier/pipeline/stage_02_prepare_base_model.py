import sys

from src.classifier.config.configuration import ConfigurationManager
from src.classifier.components.prepare_base_model import PrepareBaseModel
from src.classifier.exception import CustomException
from src.classifier.logger import logging


Stage_Name = 'Prepare base model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == '__main__':
    try:
        logging.info(f"stage {Stage_Name} has started")
        obj= PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f"stage {Stage_Name} has completed")
    except Exception as e:
        logging.info(e)
        raise CustomException(e, sys)
