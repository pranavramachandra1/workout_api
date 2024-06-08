import pandas as pd
import numpy as np
from datetime import datetime
import os

from weight_lifting import *
from metrics import *

class Query:

    def __init__(self):
        self.user_object = WorkoutData()
    
    def get_movement_name(self, movement_name: str):
        """
        Args: movement_name (str): movement user is searchign for

        Output: (pd.DataFrame): workout data with only that movement name.
        """
        df = self.user_object.weight_lifting_data
        return df[df['Movement Name'] == movement_name]
    
    def get_data_from_workout(self, workout_name = None, date = None):
        df = self.user_object.weight_lifting_data
        if workout_name:
            df = df[df['Workout Name'] == workout_name]
        if date:
            df = df
        return df
    
    def get_last_workout_data(self):
        sorted_by_date = self.user_object.weight_lifting_data.sort_values(by = 'Date', ascending = True)
        last_date = sorted_by_date['Date'].tolist()[-1]
        return sorted_by_date[sorted_by_date['Date'] == last_date]
    
    def get_volume_by_date(self):
        data = self.user_object.weight_lifting_data
        return data.groupby(['Movement Name', 'Date']).apply(volume).reset_index().rename(columns = {0: "Volume"})
    
    def get_all_volume_by_date(self):
        data = self.user_object.weight_lifting_data
        return data.groupby(['Date']).apply(volume).reset_index().rename(columns = {0: "Volume"})
