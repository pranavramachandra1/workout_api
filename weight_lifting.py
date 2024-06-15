import pandas as pd
import numpy as np
from datetime import datetime
import os

WORKOUT_DATA_PATH = "weight_lifting_data.csv"
WORKOUT_PLAN_PATH = "workout_plan.csv"

NEW_WORKOUT_DATA_PATH = "new_workout_data.csv"
NEW_WORKOUT_PLAN_PATH = "new_workout_plan.csv"

WORKOUT_DATA_COLUMNS = ['Movement Name', 'Set Number', 'Weight', 'Reps', 'Date','Workout Name']
WORKOUT_PLAN_COLUMNS = ['Workout Name', 'Movement Name', 'Sets', 'Reps', 'Date', 'Notes']

class WorkoutData:

    def __init__(self):
        
        if not os.path.exists(WORKOUT_DATA_PATH) or not os.path.exists(WORKOUT_PLAN_PATH):
            print('Please run __init__.py before creating a WorkoutData instance!')
            return None

        self.weight_lifting_data = pd.read_csv('weight_lifting_data.csv')
        self.workout_plan = pd.read_csv('workout_plan.csv')
    
    def get_weight_lifting_data(self):
        return self.weight_lifting_data
    
    def get_workout_plan(self):
        return self.workout_plan
    
    def generate_workout_template(self, workout_name):
        workout_plan = self.workout_plan[self.workout_plan['Workout Name'] == workout_name]
        num_rows = workout_plan['Sets'].sum()
        columns = self.weight_lifting_data.columns
        
        output = pd.DataFrame(index=range(num_rows), columns=columns)
        ind = 0
        for _, row in workout_plan.iterrows():
            for s in range(row['Sets']):
                output.iloc[ind] = [row['Movement Name'], s, None, None, datetime.now(), workout_name]
                ind += 1
        output.to_csv('new_workout_data.csv')
        os.system("open new_workout_data.csv")
    
    def create_new_workout(self):
        output = pd.DataFrame(columns = ['Workout Name', 'Movement Name', 'Sets', 'Reps', 'Date', 'Notes'])
        print(output.columns)
        output.to_csv('new_workout_plan.csv', index = False)
        os.system("open new_workout_plan.csv")
    
    def upload_new_workout_plan(self):
        new_plan = pd.read_csv(NEW_WORKOUT_PLAN_PATH)
        self.workout_plan = pd.concat([self.workout_plan, new_plan])
        self.workout_plan.to_csv(WORKOUT_PLAN_PATH, index=False)
        self.reprocess_workout_plan()
        print('Workout Uploaded!')
    
    def create_new_workout_data(self):
        output = pd.DataFrame(columns = self.weight_lifting_data.columns.tolist()[1:])
        output.to_csv('new_workout_data.csv')
        os.system("open new_workout_data.csv")

    def upload_workout(self):
        new_workout = pd.read_csv(NEW_WORKOUT_DATA_PATH)
        self.weight_lifting_data = pd.concat([self.weight_lifting_data, new_workout])
        self.weight_lifting_data.to_csv(WORKOUT_DATA_PATH)
        self.reprocess_workout_data()
        print('Workout Uploaded!')
    
    def reprocess_workout_plan(self):
        df = pd.read_csv(WORKOUT_PLAN_PATH)
        df = df[WORKOUT_PLAN_COLUMNS]
        df.to_csv('workout_plan.csv')

    def reprocess_workout_data(self):
        df = pd.read_csv(WORKOUT_DATA_PATH)
        df = df[WORKOUT_DATA_COLUMNS]
        df.to_csv('weight_lifting_data.csv')