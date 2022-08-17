import requests
import Api_Key
#from pprint import pprint as pp

'''
GET /v1/ohlcv/{symbol_id}
/history?period_id={period_id}
&time_start={time_start}
&time_end={time_end}
&limit={limit}
&include_empty_items={include_empty_items}'
'''

'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_{ticker}_USD/history?period_id=1MIN&time_start=2016-01-01T00:00:00'

ticker = input('Enter the symbol/ticker : ')
time_frame = '1MTH'
try: 

    url = f'https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_{ticker.upper()}_USD/history?period_id={time_frame}&time_start=2016-01-01T00:00:00'
except:
    print('Invalid symbol entered')
header = {'X-CoinAPI-Key' : Api_Key.key}
response = requests.get(url, headers=header)

data = response.json()
#pp(list(response.json()[1].items())[-1][1]) #take last key in dictonary(i.e. which is volume) then append in a list. 2016 feb first
#dictonaries inside list
volume = []

for i in range(len(data)) :
    volume.append(list(data[i].items())[-1][1])

start_date = (str(list(data[0].items())[0][1])[:10])

if __name__ == '__main__':
    #print(volume[0])
    print(str(list(data[0].items())[0][1])[:10])


