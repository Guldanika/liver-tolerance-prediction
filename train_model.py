# Full training pipeline — run with `python train_model.py`

import os
import requests
import gzip
import shutil
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from scipy.stats import ttest_ind
from lightgbm import LGBMClassifier

# ... (весь код train_model.py из моего предыдущего сообщения) ...
