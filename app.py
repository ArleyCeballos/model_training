from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import joblib
import pandas as pd

app = FastAPI()

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load('/model/model.joblib')  # Actualiza con la ruta correcta

@app.post("/score")
async def score(file: UploadFile = File(...)):
    if model is None:
        return JSONResponse(content={'error': 'Model not loaded'}, status_code=500)

    df = pd.read_csv(file.file)
    predictions = model.predict(df)
    return {"predictions": predictions.tolist()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)

