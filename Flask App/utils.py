import requests
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd

statesDic = {

    'mh': 'Maharashtra',
    'gj':'Gujarat',
    'dl':'Delhi',
    'tn':'Tamil Nadu',
    'rj':'Rajasthan',
    'mp':'Madhya Pradesh',
    'up':'Uttar Pradesh',
    'ap':'Andhra Pradesh',
    'pb':'Punjab',
    'wb':'West Bengal',
    'tg':'Telangana',
    'jk':'Jammu and Kashmir',
    'ka':'Karnataka',
    'hr':'Haryana',
    'br':'Bihar',
    'kl':'Kerala',
    'or':'Odisha',
    'ch':'Chandigarh',
    'jh':'Jharkhand',
    'tr':'Tripura',
    'ut':'Uttarakhand',
    'ct':'Chhattisgarh',
    'as':'Assam',
    'hp':'Himachal Pradesh',
    'la':'Ladakh',
    'an':'Andaman and Nicobar Islands',
    'ml':'Meghalaya',
    'py':'Puducherry',
    'ga':'Goa',
    'mn':'Manipur',
    'mz':'Mizoram',
    'ar':'Arunachal Pradesh',
    'dn':'Dadra and Nagar Haveli',
    'nl':'Nagaland',
    'sk':'Sikkim',
    'ld':'Lakshadweep',
    'dd':'Daman and Diu'
}
inv_map = {v: k for k, v in statesDic.items()}
inv_map = {k.lower(): v for k, v in inv_map.items()}

def preprocess_statedata():
    url = "https://api.covid19india.org/states_daily.json"
    data = requests.get(url)
    data = data.json()
    df = json_normalize(data['states_daily'])
    states = list(set(df.columns)-set(['status','date']))
    df.replace('', 0, inplace=True)
    df[states] = df[states].astype(int)
    return df

def preprocess_districtdata():
    url1= "	https://api.covid19india.org/zones.json"
    datadis = requests.get(url1)
    datadis = datadis.json()
    dfzones = json_normalize(datadis['zones'])
    dfzones['district'] = dfzones['district'].str.lower()
    return dfzones

def getStateCases(df,loc):
    #print("### Getting Info of {}".format(loc))
    
    latestDate = str(df['date'].iloc[[-1]]).split(' ')[4].split("\n")[0]
    
    #print("location got",loc)
    loc = inv_map[loc]
    #print("location changed to",loc)

    confCases = df[df['status']=='Confirmed'][loc].sum()
    recoverCases = df[df['status']=='Recovered'][loc].sum()
    decCases = df[df['status']=='Deceased'][loc].sum()
    activeCases = confCases - recoverCases - decCases

    obj =   {
       
        'name':str(statesDic[loc]),
        'confirmed':str(confCases),
        'recovered':str(recoverCases),
        'deceased': str(decCases),
        'active':str(activeCases),
        'date':str(latestDate)
    }
    return obj

def totalCases(df,dt):
    ttConfirmed = str(df[(df['date']==dt)&(df['status']=='Confirmed')]['tt']).split(' ')[4].split("\n")[0]
    ttrecovered = str(df[(df['date']==dt)&(df['status']=='Recovered')]['tt']).split(' ')[4].split("\n")[0]
    ttdeceased = str(df[(df['date']==dt)&(df['status']=='Deceased')]['tt']).split(' ')[4].split("\n")[0]
    
    obj ={
        'date':str(dt),
        'confirmed':str(ttConfirmed),
        'recovered':str(ttrecovered),
        'deceased':str(ttdeceased)
    }
    
    return obj    

def growthRateStates(df,loc):
    latestDate = str(df['date'].iloc[[-1]]).split(' ')[4].split("\n")[0]
    
    loc = inv_map[loc]

    confCases = df[df['status']=='Confirmed'][loc].sum()
    NoOfDays = df.shape[0]/3
    
    growthRate = (confCases)/(NoOfDays)
    
    obj={
        'name': str(statesDic[loc]),
        'growthrate': str(growthRate) + ' cases per day'    
    }
    
    return obj

def highestGrowthRateState(df):
    highest ={}
    latestDate = str(df['date'].iloc[[-1]]).split(' ')[4].split("\n")[0]
    
    states = list(set(df.columns)-set(['status','date']))
    for i in states:
        highest[i] = df[df['status']=='Confirmed'][i].sum()
    
    highest.pop('tt',None)
    Keymax = max(highest, key=highest.get) 
    statename = statesDic[Keymax]
    
    obj ={
        'name':str(statename),
        'date':str(latestDate)
    }
    return obj

def getZoneType(dfzones,dis):
    
    district = str(dfzones[dfzones['district']==dis]['district']).split(' ')[4].split("\n")[0]
    updateDate = str(dfzones[dfzones['district']==dis]['lastupdated']).split(' ')[4].split("\n")[0]
    zone = str(dfzones[dfzones['district']==dis]['zone']).split(' ')[4].split("\n")[0]
    
    obj = {
        'district':str(district),
        'updatedate':str(updateDate),
        'zone':str(zone)
    }
    
    return obj






