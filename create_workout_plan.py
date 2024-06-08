from weight_lifting import *

w = WorkoutData()
if w:
    w.create_new_workout()
else:
    print('Please run __init__.py to create a valid WorkoutData instance!')
