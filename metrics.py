import pandas as pd
import numpy as np
from datetime import datetime

from weight_lifting import *
from query import *


"""
These are a list of metrics that are calculated from passing in a single 
pd.DataFrame object. 
"""

def volume(df: pd.DataFrame) -> int:
    """
    Get the volume of a dataframe of workout data. 
    Volume = reps * weight.
    Total volume = set1_volume + set2_volume + ... 
    
    Args:
        df (pd.DataFrame): Data to be processed.
    
    Output:
        (int): Volume of the data.
    """

    return sum(df.apply(volume_helper))

def volume_helper(row):
    total += row['Weight'] * row['Reps']
    return total