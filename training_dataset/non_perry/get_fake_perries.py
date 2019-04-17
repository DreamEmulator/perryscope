import requests

for index in range(10000):
    image_json = requests.get("https://api.thecatapi.com/v1/images/search").json()
    image_url = image_json[0]["url"]
    r = requests.get(image_url)
    with open("fake_perry_" + str(index) + ".jpg", 'wb') as f:
        f.write(r.content)