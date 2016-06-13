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
               test_path='../data/test.csv',
               s = 1000000):
    '''function that sub sample the original dataset 
    '''

    random.seed(123456)
    n_train, n_test =  74180464, 6999251  #number of rows 
    small_train = '../small_data/train_' + str(s) + '.csv'
    small_test = '../small_data/test_' + str(s) + '.csv'

    # random sample train data
    skip = sorted(random.sample(xrange(1,n_train),n_train-s))
    df = pd.read_csv(train_path, skiprows=skip)
    df.columns = ['WeekNum', 'StoreID', 'ChannelID', 'RouteID', 'ClientID', 'ProductID',
             'Sales_unit_this_week', 'Sales_revenue_this_week',
             'Returns_unit_next_week', 'Returns_revenue_next_week', 
             'AdjDemand']
    df.to_csv(small_train,index=False)

    # random sample test data
    skip = sorted(random.sample(xrange(1,n_test),n_test-s))
    df = pd.read_csv(test_path, skiprows=skip)
    
    df.columns = ['id', 'WeekNum', 'StoreID', 'ChannelID', 'RouteID', 'ClientID', 'ProductID']
    df.to_csv(small_test,index=False)


def proc_prod(prod_path='../data/producto_tabla.csv'):
    '''funtion that extracts weight info to the product 


    '''

    df_prod = pd.read_csv(prod_path)
    df_prod.columns = ['ProductID', 'ProductName']
    df_prod['brand'] = df_prod['ProductName'].str.split(' ').str[-2]
    
    weight =  df_prod['ProductName'].str.extract('(\d+)(g|Kg|ml|kg|G)',expand=False)
    weight[0] = weight[0].astype('float')
    df_prod['weight'] =  np.where(weight[1].isin(['Kg','kg']), 1000 * weight[0],weight[0])
    
    
    df_prod['Vanila'] =  df_prod['ProductName'].str.contains('Vai?nill')
    df_prod.to_csv('../data/preprocessed_products.csv', index = False)