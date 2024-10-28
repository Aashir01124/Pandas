import pandas as pd 
import numpy as np

examData = {'name': ["Aashir", "Aarav", "Aarjan", "Aarogya", "Yalamber", "Manogya", "Yash", "Vedant", "Baibav", "Pratham"],
            'score': [12.5, 9, 16.5, np.nan, 9, 28, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(examData, index=labels)
print("Summary of the basic information about this DataFrame and its data: " )
print(df.info())
print(df)