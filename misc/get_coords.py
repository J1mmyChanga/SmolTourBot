import requests


def get_coords(address):
    base_url = 'https://geocode-maps.yandex.ru/1.x/'
    params = {
        'apikey': '4601ac7c-9c3f-4639-866f-0f9d3d384b00',
        'format': 'json',
        'geocode': address,
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    try:
        coordinates_str = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        latitude, longitude = map(float, coordinates_str.split())
        return latitude, longitude
    except (KeyError, IndexError, ValueError):
        return None