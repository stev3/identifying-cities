import urllib
import urllib.request
import numpy as np
import json
import time
import os

key = os.environ['GOOGLE_STREETVIEW_KEY']

new_york_bb = {
    'northeast': (40.586433,-73.699151),
    'northwest': (40.586433,-74.040070),
    'southeast': (40.905415,-73.699151),
    'southwest': (40.905415,-74.040070)
}

lats = list(np.linspace(new_york_bb['northeast'][0], new_york_bb['southeast'][0], 1000))
lons = list(np.linspace(new_york_bb['northeast'][1], new_york_bb['northwest'][1], 1000))
lats_lons = np.array(list(zip(lats,lons)))
for lat, lon in lats_lons:
    location = '{},{}'.format(lat.round(6),lon.round(6))
    time.sleep(2)
    URLCHECK = 'https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location={}&key={}'.format(location,key)
    response = urllib.request.urlopen(URLCHECK)
    data = json.load(response)
    if data['status'] == 'OK':
        URL = 'https://maps.googleapis.com/maps/api/streetview?size=640x640&location={}&key={}'.format(location,key)
        urllib.request.urlretrieve(URL, 'imgs/new_york/{}.jpg'.format(location))

tokyo_bb = {
    'northeast': (35.744823,139.837932),
    'northwest': (35.744823,139.619069),
    'southeast': (35.629466,139.837932),
    'southwest': (35.629466,139.619069)
}

lats = list(np.linspace(tokyo_bb['northeast'][0], tokyo_bb['southeast'][0], 1000))
lons = list(np.linspace(tokyo_bb['northeast'][1], tokyo_bb['northwest'][1], 1000))
lats_lons = np.array(list(zip(lats,lons)))

for lat, lon in lats_lons:
    location = '{},{}'.format(lat.round(6),lon.round(6))
    time.sleep(2)
    URLCHECK = 'https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location={}&key={}'.format(location,key)
    response = urllib.request.urlopen(URLCHECK)
    data = json.load(response)
    if data['status'] == 'OK':
        URL = 'https://maps.googleapis.com/maps/api/streetview?size=640x640&location={}&key={}'.format(location,key)
        urllib.request.urlretrieve(URL, 'imgs/tokyo/{}.jpg'.format(location))

amsterdam_bb = {
    'northeast': (52.398344,4.974490),
    'northwest': (52.398344,4.810930),
    'southeast': (52.333207,4.974490),
    'southwest': (52.333207,4.810930)
}

lats = list(np.linspace(amsterdam_bb['northeast'][0], amsterdam_bb['southeast'][0], 1000))
lons = list(np.linspace(amsterdam_bb['northeast'][1], amsterdam_bb['northwest'][1], 1000))
lats_lons = np.array(list(zip(lats,lons)))

for lat, lon in lats_lons:
    location = '{},{}'.format(lat.round(6),lon.round(6))
    URLCHECK = 'https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location={}&key={}'.format(location,key)
    response = urllib.request.urlopen(URLCHECK)
    data = json.load(response)
    time.sleep(2)
    if data['status'] == 'OK':
        URL = 'https://maps.googleapis.com/maps/api/streetview?size=640x640&location={}&key={}'.format(location,key)
        urllib.request.urlretrieve(URL, 'imgs/amsterdam/{}.jpg'.format(location))

boulder_bb = {
    'northeast': (40.057019, -105.209169),
    'northwest': (40.057019, -105.294920),
    'southeast': (39.968290, -105.209169),
    'southwest': (39.968290, -105.294920)
}

lats = list(np.linspace(boulder_bb['northeast'][0], boulder_bb['southeast'][0], 1000))
lons = list(np.linspace(boulder_bb['northeast'][1], boulder_bb['northwest'][1], 1000))
lats_lons = np.array(list(zip(lats,lons)))

for lat, lon in lats_lons:
    location = '{},{}'.format(lat.round(6),lon.round(6))
    URLCHECK = 'https://maps.googleapis.com/maps/api/streetview/metadata?size=640x640&location={}&key={}'.format(location,key)
    response = urllib.request.urlopen(URLCHECK)
    data = json.load(response)
    time.sleep(2)
    if data['status'] == 'OK':
        URL = 'https://maps.googleapis.com/maps/api/streetview?size=640x640&location={}&key={}'.format(location,key)
        urllib.request.urlretrieve(URL, 'imgs/boulder/{}.jpg'.format(location))

