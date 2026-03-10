import urllib.request
import urllib.parse
import json

# Base API URL
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # Prepare the parameters
    params = {'q': address}
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()

    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js or len(js['features']) == 0:
        print('==== Failure To Retrieve or No Results ====')
        continue

    # Get the first plus_code if available
    first_feature = js['features'][0]
    plus_code = first_feature.get('properties', {}).get('plus_code')

    if plus_code:
        print('Plus code:', plus_code)
    else:
        print('No plus code found.')
