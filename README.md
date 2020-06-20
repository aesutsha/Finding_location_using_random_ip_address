# Finding_location_using_random_ip_address
This is a python script which generates random IP address and finding out the geolocation of that IP using API.
The api used in these script is open sourced which was collected from https://freegeoip.app/
and https://geopy.readthedocs.io/en/stable/#geopy-2-0

The freegeoip api can search 15000 ip addresses in an hour. 
The ip addresses used in this script are made by using random number generator collected from the
following: https://stackoverflow.com/questions/21014618/python-randomly-generated-ip-address-as-string

location.py generates a random ip address and get geolocation information of that ip address.

finding_location_advanced.py called the geopy api and get more geolocation information from the latitude and longitude
information which was derived from freegeoip.app. Also, it creates 100 random ip address and get the geolocation info 
in json format. Then, append the valid ip addresses (if latitude is 0.0000 considered invalid) in .csv file every time
the script is executed.  
