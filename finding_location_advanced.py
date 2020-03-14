"""
Created by: Abid Ebna Saif Utsha
Date      : 12 March 2020
The api used in these script is open sourced collected from https://freegeoip.app/
The above api can search 15000 ip addresses in an hour
The ip addresses used in this script are made by using random number generator collected from 
following: https://stackoverflow.com/questions/21014618/python-randomly-generated-ip-address-as-string
"""
import requests
import pandas as pd
import numpy as np
import json
import random
import socket
import struct
from geopy.geocoders import Nominatim
import os.path

def getting_ip_address():
    """This function returns a list of random IP address"""
    new, explored=[],[]
    i=0
    while i<100:
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        if ip in explored:
            continue
        else:
            new.append(ip)
        i+=1
    new = pd.DataFrame(new, columns=['ip'])
    return new

def getting_ip(row):
    """This function calls the api and return the response"""
    url = f"https://freegeoip.app/json/{row}"       # getting records from getting ip address
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers)
    respond = response.text
    respond = json.loads(respond)
    return respond

def getting_city_nominatim(row):
    """This function calls the geopy api and return the json address output"""
    try:
        lat = row['latitude']
        lon = row['longitude']
        geolocator = Nominatim(user_agent="my-application")
        location = geolocator.reverse(f"""{lat},{lon}""")
        address = location.raw['address']
        return address
    except:
        print('timeout')

def get_information():
    """This function calls both api and add information to the pandas dataframe column"""
    new = getting_ip_address()
    new['info'] = new['ip'].apply(lambda row: getting_ip(row))
    new['time_zone'] = new['info'].apply(lambda row: row['time_zone'])
    new['latitude'] = new['info'].apply(lambda row: row['latitude'])
    new['longitude'] = new['info'].apply(lambda row: row['longitude'])
    new = new[new['latitude']!=0]
    new['address'] = new.apply(lambda row: getting_city_nominatim(row),axis=1)
    return new

def append_to_existing_df(new):
    """This function appends the new ip addresses to the dataframe"""
    if os.path.isfile(r'G:\projects\finding location\location_of_ip_address.csv'):
        new.to_csv('location_of_ip_address.csv', mode='a', header=False)
    else:
        new.to_csv('location_of_ip_address.csv', mode='w', header=True, columns=['ip','info','time_zone','latitude','longitude','address'])

def deleting_duplicate_entries():
    """This function makes sure there are no duplicate ip addresses saved in the csv file"""
    df = pd.read_csv('location_of_ip_address.csv')
    df.sort_values('ip',inplace=True)
    df.drop_duplicates(subset='ip',keep='first',inplace=True)
    df.drop(['Unnamed: 0'],axis=1,inplace=True)
    df.to_csv('location_of_ip_address.csv')

def main():
    """main function"""
    new = get_information()
    append_to_existing_df(new)
    deleting_duplicate_entries()

if __name__ == '__main__':
    main()
