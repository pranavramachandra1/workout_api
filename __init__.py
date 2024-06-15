import pandas as pd
import numpy as np
from datetime import datetime
from weight_lifting import *
import os

WORKOUT_DATA_COLUMNS = ['Movement Name', 'Set Number', 'Weight', 'Reps', 'Date','Workout Name']
WORKOUT_PLAN_COLUMNS = ['Workout Name', 'Movement Name', 'Sets', 'Reps', 'Date', 'Notes']

def valid_data_file():
    """
    Checks if weight_lifting_data.csv exists and is formatted properly.
    """
    if not os.path.exists('weight_lifting_data.csv'):
        return False
    weight_lifting_data = pd.read_csv('weight_lifting_data.csv')
    if not all([x in weight_lifting_data.columns.tolist() for x in WORKOUT_DATA_COLUMNS]):
        return False
    return True

def valid_plan_file():
    """
    Checks if workout_plan.csv exists and is formatted properly.
    """
    if not os.path.exists('workout_plan.csv'):
        return False
    workout_plan = pd.read_csv('workout_plan.csv')
    if not all([x in workout_plan.columns.tolist() for x in WORKOUT_PLAN_COLUMNS]):
        return False
    return True

breakpoint()
# Check if path for workout data exists:
if not os.path.exists('weight_lifting_data.csv') or not valid_data_file():
    weight_lifting_data = pd.DataFrame(columns = WORKOUT_DATA_COLUMNS)
    weight_lifting_data.to_csv('weight_lifting_data.csv')
    print('weight_lifting_data.csv created!')
else:
    print('weight_lifting_data.csv ready to go!')

# Check if path for workout plan exists:
if not os.path.exists('workout_plan.csv') or not valid_plan_file():
    weight_lifting_data = pd.DataFrame(columns = WORKOUT_PLAN_COLUMNS)
    weight_lifting_data.to_csv('workout_plan.csv')
    print('workout_plan.csv created!')
else:
    print('workout_plan.csv ready to go!')
