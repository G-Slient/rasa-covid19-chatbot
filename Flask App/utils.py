import requests
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from datetime import datetime

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




def check_date(dt):
    correctDate = None
    try:
        newDate = datetime.strptime(dt, '%d-%b-%y')
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate

def formatDate(dt):
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    m = str(process.extract(str(dt).split(" ")[1], months, limit=1)[0][0])

    y = '20' # Assuming year is not given by user so for now it is hardcoded for 2020 only
    d = str(dt).split(" ")[0]
    # Backend data requires day to be two digits eg: 02
    if(len(d)==1): 
        d="0"+d

    dt = str(d)+"-"+m+"-"+str(y)
    return dt

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
    
    latestDate = df['date'].iloc[[-1]].values[0]
    
    #Spelling correct with fuzzy
    print("location before spelling",loc)
    choices = statesDic.values()
    loc = str(process.extract(loc, choices, limit=1)[0][0])
    loc = loc.lower()

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
    print("Date",dt)
    #Different Format Dates
    dt = formatDate(dt)
    
    if((check_date(dt)) and (datetime.strptime(dt,'%d-%b-%y')<datetime.now())):

        ttConfirmed = df[(df['date']==dt)&(df['status']=='Confirmed')]['tt'].values[0]
        ttrecovered = df[(df['date']==dt)&(df['status']=='Recovered')]['tt'].values[0]
        ttdeceased = df[(df['date']==dt)&(df['status']=='Deceased')]['tt'].values[0]
        
        obj ={
            'status':'1',
            'date':str(dt),
            'confirmed':str(ttConfirmed),
            'recovered':str(ttrecovered),
            'deceased':str(ttdeceased)
        }
    else:
        obj={
            'status':'0'
        }

    return obj    

def growthRateStates(df,loc):
    latestDate = df['date'].iloc[[-1]].values[0]
    
    #Spelling correct with fuzzy
    print("location before spelling",loc)
    choices = statesDic.values()
    loc = str(process.extract(loc, choices, limit=1)[0][0])
    loc = loc.lower()

    loc = inv_map[loc]

    confCases = df[df['status']=='Confirmed'][loc].sum()
    NoOfDays = df.shape[0]/3
    
    growthRate = int((confCases)/(NoOfDays))
    
    obj={
        'name': str(statesDic[loc]),
        'growthrate': str(growthRate) + ' cases per day'    
    }
    
    return obj

def highestGrowthRateState(df):
    highest ={}
    latestDate = df['date'].iloc[[-1]].values[0]
    
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
    
    #Spelling check for district names
    choices = list(dfzones['district'].unique())
    dis = str(process.extract(dis, choices, limit=1)[0][0])


    district = dfzones[dfzones['district']==dis]['district'].values[0]
    updateDate = dfzones[dfzones['district']==dis]['lastupdated'].values[0]
    zone = dfzones[dfzones['district']==dis]['zone'].values[0]
    state = dfzones[dfzones['district']==dis]['state'].values[0]
    
    obj = {
        'district':str(district),
        'updatedate':str(updateDate),
        'zone':str(zone),
        'state':str(state)
    }
    
    return obj






