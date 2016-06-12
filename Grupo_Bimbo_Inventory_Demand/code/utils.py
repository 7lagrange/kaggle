import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import random

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

def sub_sample(train_path='../data/train.csv',
               test_path='../data/test.csv'):
    random.seed(123456)
    n_train, n_test =  74180464, 6999251  #number of rows 
    s = 10000 #desired sample size

    skip = sorted(random.sample(xrange(1,n_train),n_train-s))
    df = pd.read_csv(train_path, skiprows=skip)
    df.to_csv("../small_data/train.csv",index=False)

    skip = sorted(random.sample(xrange(1,n_test),n_test-s))
    df = pd.read_csv(test_path, skiprows=skip)
    df.to_csv("../small_data/test.csv",index=False)


def proc_prod(prod_path='../data/producto_tabla.csv'):
    '''
    '''
    df_prod = pd.read_csv(prod_path)