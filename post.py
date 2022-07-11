import requests


class Post:

    @staticmethod
    def blog():
        response = requests.get(url="https://api.npoint.io/f39187afba4c1903378c")
        data = response.json()
        return data