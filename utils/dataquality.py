import pandas as pd
import numpy as np

def data_quality(dataframe):
    """
    Function to evaluate the quality of the data.
    """
    # Check if there are missing values in the dataframe
    if dataframe.isnull().sum().sum() > 0:
        print("The dataframe contains missing values.")
    else:
        print("The dataframe does not contain missing values.")
    
    # Check if there are duplicate values in the dataframe
    if dataframe.duplicated().sum() > 0:
        print("The dataframe contains duplicate values.")
    else:
        print("The dataframe does not contain duplicate values.")
    
    # Check if there are non-numeric values in the dataframe
    if not np.issubdtype(dataframe.dtypes, np.number):
        print("The dataframe contains values that are not numeric.")
    else:
        print("The dataframe only contains numeric values.")


