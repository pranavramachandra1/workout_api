import pandas as pd
import numpy as np
from datetime import datetime
from weight_lifting import *
import os

def valid_data_file():
    if not os.path.exists('weight_lifting_data.csv'):
        return False
    weight_lifting_data = pd.read_csv('weight_lifting_data.csv')
    if not (weight_lifting_data.columns.tolist() == ['Movement Name', 'Set Number', 'Weight', 'Reps', 'Date','Workout Name']):
        return False
    return True

def valid_plan_file():
    if not os.path.exists('workout_plan.csv'):
        return False
    workout_plan = pd.read_csv('workout_plan.csv')
    if not (workout_plan.columns.tolist() == ['Workout Name', 'Movement Name', 'Sets', 'Reps', 'Date', 'Notes']):
        return False
    return True

# Check if path for workout data exists:
if not os.path.exists('weight_lifting_data.csv') or not valid_data_file():
    # weight_lifting_data = pd.DataFrame(columns = ['Movement Name', 'Set Number', 'Weight', 'Reps', 'Date','Workout Name'])
    # weight_lifting_data.to_csv('weight_lifting_data.csv')
    print('weight_lifting_data.csv created!')
else:
    print('weight_lifting_data.csv ready to go!')

# Check if path for workout plan exists:
if not os.path.exists('workout_plan.csv') or not valid_data_file():
    # weight_lifting_data = pd.DataFrame(columns = ['Workout Name', 'Movement Name', 'Sets', 'Reps', 'Date', 'Notes'])
    # weight_lifting_data.to_csv('workout_plan.csv')
    print('workout_plan.csv created!')
else:
    print('workout_plan.csv ready to go!')
