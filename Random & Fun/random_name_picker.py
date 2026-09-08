import requests

url = "https://randomuser.me/api/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    person = data["results"][0]
    first_name = person["name"]["first"]
    last_name = person["name"]["last"]
    country = person["location"]["country"]

    print(f"Name: {first_name} {last_name}")
    print(f"Country: {country}")
else:
    print("Could not get a random name.")
