from fastapi import FastAPI
from starlette.responses import JSONResponse
from joblib import load
import pandas

app = FastAPI()

gmm_pipe = load("../models/gmm_pipe.joblib")

