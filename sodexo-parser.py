import json
import requests
import time
from termcolor import colored

RESTAURANT_ID = 878

date = time.strftime("%Y/%m/%d")

response = requests.get('http://www.sodexo.fi/ruokalistat/output/daily_json/' + str(RESTAURANT_ID) + '/' + date + '/fi')
json_data = json.loads(response.text)

for entry in json_data['courses']:

    # There might be other than menu rows, skip them
    if 'category' in entry and 'title_fi' in entry:
        dish = colored('{0: <15}'.format(entry['category']), 'yellow') + entry['title_fi']
        if 'price' in entry:
            dish += colored(' (' + entry['price'] + ')', 'red')
        print dish
