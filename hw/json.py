json_string = """{"organisation": "Python Software Foundation",
                 "officers": [
                            {"first_name": "Guido", "last_name":"Rossum", "position":"president"},
                            {"first_name": "Diana", "last_name":"Clarke", "position":"chair"},
                            {"first_name": "Naomi", "last_name":"Ceder", "position":"vice chair"},
                            {"first_name": "Van", "last_name":"Lindberg", "position":"vice chair"},
                            {"first_name": "Ewa", "last_name":"Jodlowska", "position":"director of operations"}
                            ],
                "type": "non-profit",
                "country": "USA",
                "founded": 2001,
                "members": 244,
                "budget": 750000,
                "url": "www.python.org/psf/"}"""

import json
data = json.loads(json_string)
#print(type(data))
#for key in data:
#    print(key, '\t', data[key])

dict_a = {"John": 21, "Kate": 27, "Bill": 29}
json_string = json.dumps(dict_a)
#print(type(json_string))
#print(json_string)

mas_a = ['fish', 'shark']
json_string = json.dumps(mas_a)
#print(type(json_string))
#print(json_string)
