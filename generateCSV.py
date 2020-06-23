import pandas as pd
import numpy as np

allParticipants = pd.DataFrame({'Age': [], 'Degree': [], 'Gender': [],
                                'Belt': [], 'Height': [], 'Weight': []})

age = np.random.randint(7, 75, size=150)

degree = []
gender = []
height = []
weight = []
belt = []

for i in range(150):
    if age[i] == 7:
        degree.append(np.random.randint(-8, -5))
    elif age[i] == 8:
        degree.append(np.random.randint(-8, -2))
    elif age[i] >= 9 and age[i] < 13:
        degree.append(np.random.randint(-8, -1))
    elif age[i] <= 13 and age[i] < 18:
        degree.append(np.random.randint(-8, 3))
    elif age[i] >= 18:
        degree.append(np.random.randint(-8, 8))
        
    if age[i] < 13:
        gender.append('Child')
        height.append(np.random.uniform(0.9, 1.5))
    elif age[i] >= 13 and age[i] < 18:
        gender.append(np.random.choice(['Boy', 'Girl']))
        height.append(np.random.uniform(1.3, 2.0))
    else:
        gender.append(np.random.choice(['Man', 'Woman']))
        height.append(np.random.uniform(1.4, 2.0))
    

    weight.append((20*pow(height[i],2)) + np.random.uniform(-1.5*pow(height[i],2), 10*pow(height[i], 2)))
    
#print(degree)    
    
for i in range(len(degree)):    
    if degree[i] == -8:
        belt.append('white')
    elif degree[i] == -7:
        belt.append('red')
    elif degree[i] == -6:
        belt.append('yellow')
    elif degree[i] == -5:
        belt.append('orange')
    elif degree[i] == -4:
        belt.append('green')
    elif degree[i] == -3:
        belt.append('blue')
    elif degree[i] == -2:
        belt.append('purple')
    elif degree[i] == -1:
        belt.append('brown')
    elif degree[i] == 0:
        degree[i] == -1
        belt.append('brown')
    else:
        belt.append('black ' + str(degree[i]))
        
allParticipants = pd.DataFrame({'Age': age[:len(degree)], 'Degree': degree, 'Gender': gender[:len(degree)],
                                'Belt': belt[:len(degree)], 'Height': height[:len(degree)], 'Weight': weight[:len(degree)]})
    
#allParticipants.to_csv('MartialArtsTornamentParticipants.csv')

