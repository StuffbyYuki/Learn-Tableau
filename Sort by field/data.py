import pandas as pd 
import random 
import numpy as np

semesters = ['201710', '201720', '201730', 
             '201810', '201820', '201830', 
             '201910', '201920', '201930',
             '202010', '202020', '202030']


values = random.sample(range(1, 100), 12)

df = pd.DataFrame({'values': values, 
                   'semester': semesters}) 

df['semester_desc'] = ( df.semester.apply(lambda x: 'Summer ' + x[:-2] if x[-2:] == '20' else x)
                        .apply(lambda x: 'Spring ' + x[:-2] if x[-2:] == '10' else x) 
                        .apply(lambda x: 'Fall ' + x[:-2] if x[-2:] == '30' else x) )

print(df)

df.to_csv('data.csv', index=None)
