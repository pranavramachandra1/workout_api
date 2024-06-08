from weight_lifting import *

w = WorkoutData()
if w:
    w.upload_new_workout_plan()
else:
    print('Please run __init__.py to create a valid WorkoutData instance!')
