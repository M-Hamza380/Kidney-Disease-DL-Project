import sys

from src.classifier.config.configuration import ConfigurationManager
from src.classifier.components.model_evaluation import Evaluation
from src.classifier.exception import CustomException
from src.classifier.logger import logging

Stage_Name = 'Model Evaluation'

class EvaluationPipeline:
    def __init__(self):
        pass

    def main():
        config = ConfigurationManager()
        eval_config = config.get_evaluate_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == '__main__':
    try:
        logging.info(f"stage {Stage_Name} has started")
        obj= EvaluationPipeline()
        obj.main()
        logging.info(f"stage {Stage_Name} has completed")
    except Exception as e:
        logging.info(e)
        raise CustomException(e, sys)


