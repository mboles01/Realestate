# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:57:21 2019

@author: BolesMi
"""

# import data cleaning functions
from cleanfunctions_realtor import address_clean, beds_clean, baths_clean, 
homesize_clean, lotsize_clean, price_clean, coords_clean, acretosqft, flatten

# clean raw data
address = address_clean(address_raw)
beds = beds_clean(beds_raw)
baths = baths_clean(baths_raw)
homesize = homesize_clean(homesize_raw)
lotsize = lotsize_clean(lotsize_raw, lotunits_raw)
price = price_clean(price_raw)
latitude, longitude = coords_clean(coords_raw)

# count up lengths of arrays to be joined
len_address = 'Address', len(address)
len_city = 'City', len(city)
len_state = 'State', len(state)
len_zip = 'Zip', len(zip_code)
len_beds = 'Beds', len(beds)
len_baths = 'Baths', len(baths)
len_homesize = 'Homesize', len(homesize)
len_lotsize = 'Lot', len(lotsize)
len_price = 'Price', len(price)
len_latitude = 'Latitude', len(latitude)
len_longitude = 'Longitude', len(longitude)

# check if any are not matching the others     
lengths = [len_address, len_city, len_state, len_zip, len_beds, len_baths, len_homesize, len_lotsize, len_price, len_latitude, len_longitude]
len_proper = max(set([item[1] for item in lengths]), key=[item[1] for item in lengths].count)
for counter, item in enumerate(lengths):
    if item[1] != len_proper:
        print('%s has improper length: %s, should be %s' % (lengths[counter][0], lengths[counter][1], len_proper))
        pass
#                return address, city, zip_code, beds, baths, homesize, lot, yearbuilt, garage, hometype, price, address_raw, beds_raw, baths_raw, lot_raw, yearbuilt_raw, garage_raw, hometype_raw, price_raw
#                sys.exit()
    else:
        pass
