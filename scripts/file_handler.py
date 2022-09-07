import json
import mlflow
import pickle
# import dvc.api
import pandas as pd
from config import Config
from log import get_logger
from time import gmtime, strftime

my_logger = get_logger("FileHandler")


class FileHandler():

  def __init__(self):
    pass
 
 
  def save_csv(self, df, csv_path, index=False):
    try:
      df.to_csv(csv_path, index=index)
      my_logger.info("file saved as csv")

    except Exception:
      my_logger.exception("save failed")

  def read_csv(self, csv_path):
    try:
      df = pd.read_csv(csv_path)
      my_logger.debug("file read as csv")
      return df
    except FileNotFoundError:
      my_logger.exception("file not found")

  def save_model(self, model, model_name):
    try:
      file_name = model_name+"_model "+ strftime("%Y-%m-%d %H-%M-%S", gmtime())
      with open(f'../models/{file_name}.pkl', 'wb') as my_model:
        pickle.dump(model, my_model) 

      mlflow.log_artifact(f"../models/{file_name}.pkl")
      my_logger.info("The model is successfully saved!")

    except Exception:
      my_logger.exception("save failed")

  def read_model(self, model_name):
    try:
      name = Config.MODELS_PATH / str(model_name + ".pkl")
      model = pickle.load(open(name, "rb"))
      my_logger.debug("model read as pkl")
      return model
      
    except FileNotFoundError:
      my_logger.exception("model not found")

  def save_metrics(self, data, file_name):
    try:
      time = strftime("%Y-%m-%d-%H:%M", gmtime())
      name = Config.METRICS_FILE_PATH / str(file_name + "-" + time + ".json")
      with open(name, 'w') as fp:
        json.dump(data, fp)
      my_logger.info("metrics saved as json")

    except Exception:
      my_logger.exception("metrics save failed")

  def read_metrics(self, file_name):
    try:
      name = Config.METRICS_FILE_PATH / str(file_name + ".json")
      res = json.load(name)
      my_logger.debug("metrics read as json")
      return res
    except FileNotFoundError:
      my_logger.exception("metrics file not found")