import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
top_countries = sorted(countries,
             key=lambda country: country['population'], reverse=True)[:10]
for c in top_countries:
    print(f"{c['name']:50} {c['region']:30}  {c['population']:10}")
