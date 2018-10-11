from urllib import request
import json
import re


with request.urlopen('http://118.24.241.17/path.json') as f:
    data = f.read()
    data_json = json.loads(data.decode('utf8'))

    x = [_[0]['x'] for _ in data_json]
    y = [_[0]['y'] for _ in data_json]
    time = [_[0]['time'] for _ in data_json]
    time_format = [re.split(',', _time) for _time in time]
    time_year = [time_format[_][0] for _ in range(len(time_format))]