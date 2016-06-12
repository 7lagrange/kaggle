import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math

# 
def rmsle(y, y_pred):
    '''A function to calculate Root Mean Squared Logarithmic Error (RMSLE)
    # https://www.kaggle.com/marknagelberg/caterpillar-tube-pricing/rmsle-function

    Parameters
    ----------
    :type y: np.array
    :param y: test y value

    :type y_pred: np.array
    :param y_pred: predicted y value

    returns
    ----------
    :type error: floats
        RMSLE for prediction


    '''
    assert len(y) == len(y_pred)
    terms_to_sum = [(math.log(y_pred[i] + 1) - math.log(y[i] + 1)) ** 2.0 for i,pred in enumerate(y_pred)]
    error  =  (sum(terms_to_sum) * (1.0/len(y))) ** 0.5
    return error 


def proc_prod(prod_path='../data/producto_tabla.csv'):
    '''
    '''
    df_prod = pd.read_csv(prod_path)