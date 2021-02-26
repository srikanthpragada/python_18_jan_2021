import requests

def get_languages(country):
    languages = country['languages']
    names = []
    for c in languages:
        names.append(c['name'])

    return ",".join(names)

def get_currencies(country):
    currencies = country['currencies']
    names = []
    for c in currencies:
        if c['name'] is not None:
           names.append(c['name'])

    return ",".join(names)


def get_borders(country):
    return ",".join(country['borders'])


code = input("Enter country code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
if resp.status_code != 200:
    print("Sorry! Invalid country code!")
    exit()

country = resp.json()

print("Name        :", country['name'])
print("Capital     :", country['capital'])
print("Region      :", country['region'])
print("Population  :", country['population'])
print("Currencies  :", get_currencies(country))
print("Border      :", get_borders(country))
print("Languages   :", get_languages(country))
