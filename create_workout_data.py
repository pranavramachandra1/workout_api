from weight_lifting import *

w = WorkoutData()
if w:
    w.create_new_workout_data()
else:
    print('Please run __init__.py to create a valid WorkoutData instance!')
