import pytest


def test__get_air_pollution_data__returns_200(client):
    response = client.get("/run-advice")
    assert b"<h2>Hello, World!</h2>" in response.data
    assert response.status_code == 200
