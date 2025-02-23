import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_converter_numero_valido():
    response = client.get("/converter/123")
    assert response.status_code == 200
    assert response.json() == {"extenso": "cento e vinte e três"}

def test_converter_zero():
    response = client.get("/converter/0")
    assert response.status_code == 200
    assert response.json() == {"extenso": "zero"}

def test_converter_numero_negativo():
    response = client.get("/converter/-1")
    assert response.status_code == 400
    assert "error" in response.json()["detail"]

def test_converter_numero_muito_grande():
    response = client.get("/converter/1000000000")
    assert response.status_code == 400
    assert "error" in response.json()["detail"]

def test_converter_entrada_invalida():
    response = client.get("/converter/abc")
    assert response.status_code == 422  # Erro de validação do FastAPI 