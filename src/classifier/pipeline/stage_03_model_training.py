import sys

from src.classifier.config.configuration import ConfigurationManager
from src.classifier.components.model_training import Trainig
from src.classifier.exception import CustomException
from src.classifier.logger import logging


Stage_Name = 'Model Training'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Trainig(config= training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logging.info(f"stage {Stage_Name} has started")
        obj= ModelTrainingPipeline()
        obj.main()
        logging.info(f"stage {Stage_Name} has completed")
    except Exception as e:
        logging.info(e)
        raise CustomException(e, sys)



