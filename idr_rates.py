import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.8414720585614e-5,"date":"Thu, 26 May 2022 11:55:01 GMT","inverseRate":14616.737325538},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":6.4112847965179e-5,"date":"Thu, 26 May 2022 11:55:01 GMT","inverseRate":15597.49772063}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])