"""
Created by: Abid Ebna Saif Utsha
Date      : 12 March 2020
The api used in these script is open sourced collected from https://freegeoip.app/
The above api can search 15000 ip addresses in an hour
The ip addresses used in this script are made by using random number generator collected from 
following: https://stackoverflow.com/questions/21014618/python-randomly-generated-ip-address-as-string
"""
import requests
import json
import random
import socket
import struct
def getting_ip_address():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


def getting_ip(ip):
    url = f"https://freegeoip.app/json/{ip}"       # getting records from getting ip address

    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }

    response = requests.request("GET", url, headers=headers)
    respond = response.text
    return respond

def returning_info(api_response):
    res = json.loads(api_response)
    ip = res['ip']
    country = res['country_name']
    state = res['region_name']
    city = res['city']
    time_zone = res['time_zone']
    lat = res['latitude']
    lon = res['longitude']
    return ip, country, city, time_zone, lat, lon
def main():
    ip_gen = getting_ip_address()
    api_response = getting_ip(ip_gen)
    ip, country, city, time_zone, lat, lon = returning_info(api_response)
    print(f"ip_address: {ip}\ncountry_name: {country}\ncity: {city}\ntime_zone: {time_zone}\nlatitude: {lat}\nlongitude: {lon}")

if __name__ == '__main__':
    main()