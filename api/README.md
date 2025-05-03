# HAL API
API for UI and other tools that need the api

## Prerequisites
Conda environmentt with python 3.13.3

### Packages
* conda install uvicorn
* conda install fastapi

## Start
uvicorn api:app --reload --host 0.0.0.0 --port 5000
curl http://localhost:5000/api?query=vad%20heter%20jag