from fastapi import FastAPI
import functools
from relationships import get_nationality, get_travel_place, get_relationship
from schema import PatientList

app = FastAPI()

@app.post("/")
def single(patients: PatientList):
    return process_records(patients)

@app.get("/status/")
def status():
    return {"status": "alive"}

def process_records(records):
    return {
        "patients": [
            {r.patientId: record_processor(r.notes)} for r in records.patients
        ]
    }

@functools.lru_cache(30000)
def record_processor(sent):
    return {
        "nationality": get_nationality(sent),
        "travel": get_travel_place(sent),
        "relationship": get_relationship(sent),
    }

