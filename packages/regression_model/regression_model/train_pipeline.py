import numpy as np
from sklearn.model_selection import train_test_split

from regression_model import pipeline
from regression_model.processing.data_management import (
    load_dataset, save_pipeline)
from regression_model.config import config
from regression_model import __version__ as _version
#pipeline file is the heart of the package
import logging


_logger = logging.getLogger(__name__)

#finction that will run train model
def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.1,
        random_state=0)  # we are setting the seed here

    # transform the target, use log format because it is expected by the sklearn pipeline
    y_train = np.log(y_train)
    y_test = np.log(y_test)

    pipeline.price_pipe.fit(X_train[config.FEATURES],
                            y_train)
    #after applying fit we save to pipeline
    _logger.info(f'saving model version: {_version}')
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == '__main__':
    run_training()
