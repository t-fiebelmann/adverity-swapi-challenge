import requests

class People():
    SWAPI_BASE_URL = 'https://swapi.dev/api/people/'
    def __init__(self):
        pass
    def get_person(self, id):
        r = requests.get(SWAPI_BASE_URL + "/{}".format(id))
        return r.json()
    def get_all_people(self):
        r = requests.get(SWAPI_BASE_URL)
        return r.json()