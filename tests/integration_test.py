import requests

def test_score_endpoint():
    # Prueba la puntuación de datos enviando un archivo CSV
    file_path = 'data/score.csv'
    with open(file_path, 'rb') as f:
        response = requests.post('http://localhost:8888/score', files={'file': f})
    assert response.status_code == 200
    assert 'predictions' in response.json()
