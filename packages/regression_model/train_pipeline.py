import pathlib
#this is new way of defining paths 
#pipeline file is the heart of the package

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

import pipeline


#directories that will be used be various functions
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent #root folder
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models' #directory where w place our trained models
DATASET_DIR = PACKAGE_ROOT / 'datasets' #specify where we find dataet direcotry

TESTING_DATA_FILE = DATASET_DIR / 'test.csv'
TRAINING_DATA_FILE = DATASET_DIR / 'train.csv'
TARGET = 'SalePrice'

#specifdy features that we are pulling from train.csv
FEATURES = ['MSSubClass', 'MSZoning', 'Neighborhood', 'OverallQual',
            'OverallCond', 'YearRemodAdd', 'RoofStyle', 'MasVnrType',
            'BsmtQual', 'BsmtExposure', 'HeatingQC', 'CentralAir',
            '1stFlrSF', 'GrLivArea', 'BsmtFullBath', 'KitchenQual',
            'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageFinish',
            'GarageCars', 'PavedDrive', 'LotFrontage',
            # this variable is only to calculate temporal variable:
            'YrSold']

#this will persist the pipeline and save to pkl file using joblib libary
def save_pipeline(*, pipeline_to_persist) -> None:
    """Persist the pipeline."""

    save_file_name = 'regression_model.pkl'
    save_path = TRAINED_MODEL_DIR / save_file_name
    joblib.dump(pipeline_to_persist, save_path)

    print('saved pipeline')

#finction that will run train model
def run_training() -> None:
    """Train the model."""

    # read training data
    data = pd.read_csv(TRAINING_DATA_FILE)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[FEATURES],
        data[TARGET],
        test_size=0.1,
        random_state=0)  # we are setting the seed here

    # transform the target, use log format because it is expected by the sklearn pipeline
    y_train = np.log(y_train)
    y_test = np.log(y_test)

    pipeline.price_pipe.fit(X_train[FEATURES],
                            y_train)
    #after applying fit we save to pipeline
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == '__main__':
    run_training()
