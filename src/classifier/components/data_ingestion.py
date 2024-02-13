import sys
import os
import zipfile
import gdown

from src.classifier.exception import CustomException
from src.classifier.logger import logging
from src.classifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self) -> str:
        '''
            fetch the data from url
        '''

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs('artifacts/data_ingestion', exist_ok= True)
            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            url = prefix+file_id
            gdown.download(url, zip_download_dir)
            logging.info(f'Downloaded data from {dataset_url} into file {zip_download_dir}')
        except Exception as e:
            print(f'Your URL found : {url}')
            raise CustomException(e, sys)
    
    def extract_zip_file(self):
        '''
            zip_file_path: str
            Extracts the zip file into the data directory
            Function returns None
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)



