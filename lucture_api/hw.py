import requests

url = 'https://api.punkapi.com/v2/beers/8'


def test_get_request():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()[0]['name'] == 'Fake Lager'
    assert response.json()[0]['abv'] == 4.7


def test_delete_request():
    response_del = requests.delete(url)
    assert response_del.status_code == 404
    assert response_del.json()['message'] == "No endpoint found that matches \'/v2/beers/8\'"
