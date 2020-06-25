# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:07:47 2020

@author: cojs2018

This application will divide the loaded dataframe into groups of size in interval [2, 8].
"""

import pandas as pd
import numpy as np

#First we need to get the data frame from the csv file
participants = pd.read_csv('MartialArtsTournamentParticipants.csv', sep=",").set_index('Participant_Number')

def divideByAge(participants):
    """
    Function will sort according to first rule, which is to divide by age.
    
    Input:
        participants: Data frame with following columns:
            Participant_Number: ID;
            Age: age of participants in years;
            Degree: grade of participant;
            Belt: color of belt;
            Gender: gender of particpant;
            Height: height of participant;
            Weight: weight of participant;
            
    Returns: data frames a1, a2, a3, a4 such that for all x in participants,
                iff x.Age < 13, x is in a1
                iff 13 <= x.Age < 18, x is in a2
                iff 18 <= x.Age < 50, x is in a3
                else x is in a4
    """
    
    a1 = participants[participants.Age < 13]
    nota1 = participants[participants.Age >= 13]
    a2 = nota1[nota1.Age < 18]
    nota2 = nota1[nota1.Age >= 18]
    a3 = nota2[nota2.Age < 50]
    a4 = nota2[nota2.Age >= 50]
    return a1, a2, a3, a4

children, teens, adults, veterans = divideByAge(participants)


def divideByGender(participants):
    """
    Function will sort according to second rule, which is to divide by gender.
    
    Input:
        participants: Data frame with following columns:
            Participant_Number: ID;
            Age: age of participants in years;
            Degree: grade of participant;
            Belt: color of belt;
            Gender: gender of particpant;
            Height: height of participant;
            Weight: weight of participant;
            
    Returns: data frames g1, g2 such that for all x in participants,
        if x.Gender is female, x is in g1
        else if x.Gender is male, x is in g2           
    """
    
    female = ["Girl", "Woman"]
    g1 = participants[np.isin(participants.Gender, female)]
    g2 = participants[np.isin(participants.Gender, female, invert=True)]
    return g1, g2

teensF, teensM = divideByGender(teens)
adultsF, adultsM = divideByGender(adults)
vetF, vetM = divideByGender(veterans)

def divideByDegree(participants):
    """
    Function will sort according to third rule, which is to divide by degree, 
    making use of a decision tree considering the distribution.
    
    Input:
        participants: Data frame with following columns:
            Participant_Number: ID;
            Age: age of participants in years;
            Degree: grade of participant;
            Belt: color of belt;
            Gender: gender of particpant;
            Height: height of participant;
            Weight: weight of participant;
            
    Returns: data frames D depending on mean and standard deviation         
    """
    #Get mean value then seperate into each group accordingly
    mu = participants.Degree.mean()
    if participants.shape[0] > 3:
        d1 = participants[participants.Degree < mu]
        d2 = participants[participants.Degree >= mu]
        return d1, d2
    else:
        return participants, []
    
ch1, ch2 = divideByDegree(children)
tF1, tF2 = divideByDegree(teensF)
tM1, tM2 = divideByDegree(teensM)
aF1, aF2 = divideByDegree(adultsF)
aM1, aM2 = divideByDegree(adultsM)
vF1, vF2 = divideByDegree(vetF)
vM1, vM2 = divideByDegree(vetM)

from sklearn.cluster import KMeans
def divideByBMI(participants):
    """
    Function will sort according to fourth rule, which is to divide by BMI 
    and/or any distance based rule found by the processor, making use of a 
    decision tree considering the distribution.
    
    Input:
        participants: Data frame with following columns:
            Participant_Number: ID;
            Age: age of participants in years;
            Degree: grade of participant;
            Belt: color of belt;
            Gender: gender of particpant;
            Height: height of participant;
            Weight: weight of participant;
            
    Returns: data frames D depending on decision tree
    """
    
    columns = ["Age", "Degree", "Height", "Weight", "Set"]
    df = pd.DataFrame({k: [] for k in columns})
    if type(participants) == type(df):
        #Calculate a BMI column for data frame using formula
        BMI = (participants.Weight / pow(participants.Height, 2))
        
        #work out appropriate number of clustors
        n = int(np.ceil(participants.shape[0] / 7))
        
        participants = participants.set_index([participants.index, "Gender", "Belt"])
        
        results = KMeans(n_clusters=n, random_state=0).fit(participants, y=None, sample_weight = np.log(BMI) / np.log(BMI.mean()))
        
        #Add cluster label onto prediction
        participants["Set"] = results.labels_.astype(str)
        
        return participants
    else:
        return df
        
chA = divideByBMI(ch1).sort_values('Set', ascending=True)
chA.Set = "chA" + chA.Set

chB = divideByBMI(ch2).sort_values('Set', ascending=True)
chB.Set = "chB" + chB.Set

tFA = divideByBMI(tF1).sort_values('Set', ascending=True)
tFA.Set = "tFA" + tFA.Set

tFB = divideByBMI(tF2).sort_values('Set', ascending=True)
tFB.Set = "tFB" + tFB.Set

tMA = divideByBMI(tM1).sort_values('Set', ascending=True)
tMA.Set = "tMA" + tMA.Set

tMB = divideByBMI(tM2).sort_values('Set', ascending=True)
tMB.Set = "tMB" + tMB.Set
   
aFA = divideByBMI(aF1).sort_values('Set', ascending=True)
aFA.Set = "aFA" + aFA.Set

aFB = divideByBMI(aF2).sort_values('Set', ascending=True)
aFB.Set = "aFB" + aFB.Set
    
aMA = divideByBMI(aM1).sort_values('Set', ascending=True)
aMA.Set = "aMA" + aMA.Set

aMB = divideByBMI(aM2).sort_values('Set', ascending=True)
aMB.Set = "aMB" + aMB.Set

vFA = divideByBMI(vF1).sort_values('Set', ascending=True)
vFA.Set = "vFA" + vFA.Set

vFB = divideByBMI(vF2).sort_values('Set', ascending=True)
vFB.Set = "vFB" + vFB.Set

vMA = divideByBMI(vM1).sort_values('Set', ascending=True)
vMA.Set = "vMA" + vMA.Set

vMB = divideByBMI(vM2).sort_values('Set', ascending=True)
vMB.Set = "vMB" + vMB.Set

final_result = pd.concat([chA, chB, tFA, tFB, tMA, tMB, aFA, aFB, aMA, aMB, vFA, vFB, vMA, vMB])

final_result.to_csv('result.csv')   