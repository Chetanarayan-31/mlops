import os
import warnings
import sys

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
import mlflow.onnx

import logging

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("model-management-demo")

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)