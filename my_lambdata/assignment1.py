import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def train_test_split(df, frac):

    '''Create a Train/Test split function for a dataframe

    and 
    
    Returns: 
    returns both the Training and Testing sets. 
    
    Frac refers to the percent of data you would like to set

    aside for training.
    '''

    data = np.array(range[0, 100, 2])
    df = pd.DataFrame(data)
    frac = train_test_split(train, train_size=.80, random_state=42)
    print("This is the dataframe maybe", frac)