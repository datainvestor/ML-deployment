import pandas as pd
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline

from regression_model.config import config
<<<<<<< HEAD
from regression_model import __version__ as _version

import logging


_logger = logging.getLogger(__name__)

=======
#centralize loading and persistence functions
>>>>>>> 7547cdf1d8aaab4883797b235bdf14551e95cf5f

def load_dataset(*, file_name: str
                 ) -> pd.DataFrame:
    _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    return _data

#this will persist the pipeline and save to pkl file using joblib libary
def save_pipeline(*, pipeline_to_persist) -> None:
    """Persist the pipeline.

    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.
    """

    # Prepare versioned save file name
    save_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
    save_path = config.TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=save_file_name)
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info(f'saved pipeline: {save_file_name}')


def load_pipeline(*, file_name: str
                  ) -> Pipeline:
    """Load a persisted pipeline."""

    file_path = config.TRAINED_MODEL_DIR / file_name
<<<<<<< HEAD
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep) -> None:
    """
    Remove old model pipelines.
    This is to ensure there is a simple one-to-one
    mapping between the package version and the model
    version to be imported and used by other applications.
    """

    for model_file in config.TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in [files_to_keep, '__init__.py']:
            model_file.unlink()
=======
    saved_pipeline = joblib.load(filename=file_path)
    return saved_pipeline
>>>>>>> 7547cdf1d8aaab4883797b235bdf14551e95cf5f
