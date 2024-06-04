import pandas as pd
import os
import joblib
import sklearn
from scripts.train_model import train_model

def test_train_model(tmpdir):
    # Cargar los datos de entrenamiento y seleccionar un subconjunto
    full_data = pd.read_csv('data/train.csv')
    data = full_data.sample(n=50)  # selecciona 50 filas al azar
    data_path = str(tmpdir.join('test_data.csv'))
    data.to_csv(data_path, index=False)
    model_save_path = str(tmpdir.join('test_model.pkl'))

    # Ejecutar la función train_model
    train_model(data_path, model_save_path)

    # Verificar que el modelo se haya guardado correctamente
    assert os.path.exists(model_save_path)

    # Cargar el modelo y verificar que es una instancia de Pipeline
    model = joblib.load(model_save_path)
    assert isinstance(model, sklearn.pipeline.Pipeline)

def test_model_with_missing_values(tmpdir):
    # Cargar los datos de entrenamiento y seleccionar un subconjunto
    full_data = pd.read_csv('data/train.csv')
    data = full_data.sample(n=50)  # selecciona 50 filas al azar
    data_path = str(tmpdir.join('test_data.csv'))
    data.to_csv(data_path, index=False)
    model_save_path = str(tmpdir.join('test_model.pkl'))

    # Ejecutar la función train_model
    train_model(data_path, model_save_path)

    # Cargar el modelo
    model = joblib.load(model_save_path)

    # Crear un conjunto de datos de prueba con valores faltantes
    test_data = full_data.sample(n=10)
    test_data = test_data.drop("y", axis=1)
    test_data.iloc[0, 0] = None  # introduce un valor faltante

    # Verificar que el modelo puede hacer predicciones con datos faltantes
    predictions = model.predict(test_data)
    assert len(predictions) == len(test_data)

def test_model_predictions(tmpdir):
    # Cargar los datos de entrenamiento y seleccionar un subconjunto
    full_data = pd.read_csv('data/train.csv')
    data = full_data.sample(n=50)  # selecciona 50 filas al azar
    data_path = str(tmpdir.join('test_data.csv'))
    data.to_csv(data_path, index=False)
    model_save_path = str(tmpdir.join('test_model.pkl'))

    # Ejecutar la función train_model
    train_model(data_path, model_save_path)

    # Cargar el modelo
    model = joblib.load(model_save_path)

    # Crear un conjunto de datos de prueba
    test_data = full_data.sample(n=10)
    test_X = test_data.drop("y", axis=1)

    # Verificar que el modelo puede hacer predicciones
    predictions = model.predict(test_X)
    assert len(predictions) == len(test_X)