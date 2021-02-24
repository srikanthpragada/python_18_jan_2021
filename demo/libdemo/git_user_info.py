import requests

user = "srikanthpragada"

resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print(f"Sorry! Could not get details of {user}!")
    exit()

details = resp.json()

for name, value in details.items():
    if value is not None:
        print(f"{name:20}  {value}")
