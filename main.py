import json
from typing import Annotated, Literal

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field

print("LOADING MY MAIN.PY")

app = FastAPI()


# ==========================
# Pydantic Model
# ==========================

class Patient(BaseModel):
    id: Annotated[
        str,
        Field(..., description="Unique identifier for the patient")
    ]

    name: Annotated[
        str,
        Field(
            ...,
            min_length=1,
            max_length=100,
            description="Name of the patient"
        )
    ]

    age: Annotated[
        int,
        Field(
            ...,
            ge=0,
            le=120,
            description="Age of the patient"
        )
    ]

    city: Annotated[
        str,
        Field(
            ...,
            min_length=1,
            max_length=100,
            description="City of the patient"
        )
    ]

    email: Annotated[
        str,
        Field(..., description="Email address of the patient")
    ]

    gender: Annotated[
        Literal["Male", "Female", "Other"],
        Field(..., description="Gender of the patient")
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            strict=True,
            description="Weight in kilograms"
        )
    ]

    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            strict=True,
            description="Height in meters"
        )
    ]

    married: Annotated[
        bool,
        Field(
            default=False,
            description="Marital status"
        )
    ]

    allergies: Annotated[
        list[str],
        Field(
            default_factory=list,
            description="List of allergies"
        )
    ]

    contact: Annotated[
        dict,
        Field(
            default_factory=dict,
            description="Emergency contact information"
        )
    ]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

    @computed_field
    @property
    def calculate_verdict(self) -> str:
        bmi = self.calculate_bmi

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal Weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"


# ==========================
# Utility Functions
# ==========================
class patient_update(BaseModel):    
    name: Annotated[
        str,
        Field(
            ...,
            min_length=1,
            max_length=100,
            description="Name of the patient"
        )
    ]

    age: Annotated[
        int,
        Field(
            ...,
            ge=0,
            le=120,
            description="Age of the patient"
        )
    ]

    city: Annotated[
        str,
        Field(
            ...,
            min_length=1,
            max_length=100,
            description="City of the patient"
        )
    ]

    email: Annotated[
        str,
        Field(..., description="Email address of the patient")
    ]


def load_data():
    with open("patients.json", "r") as file:
        return json.load(file)


def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file, indent=4)


# ==========================
# Routes
# ==========================

@app.get("/")
def home():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {
        "message": "This is the About page for the Patient Management System."
    }


@app.get("/view")
def view_patients():
    return load_data()


@app.get("/patient/{patient_id}")
def get_patient(
    patient_id: str = Path(
        ...,
        description="Patient ID",
        examples={"example": "P001"},
    )
):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} not found"
        )

    return data[patient_id]


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort by Height, Weight, or BMI"
    ),
    order: str = Query(
        "asc",
        description="Sort order: asc or desc"
    ),
):
    valid_sort_fields = ["Height", "Weight", "BMI"]

    if sort_by not in valid_sort_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Valid fields are {valid_sort_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be either 'asc' or 'desc'"
        )

    data = load_data()

    sorted_data = sorted(
        data.values(),
        key=lambda patient: patient.get(sort_by, 0),
        reverse=(order == "desc"),
    )

    return sorted_data


@app.post("/create_patient", status_code=201)
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail=f"Patient with ID {patient.id} already exists"
        )

    data[patient.id] = patient.model_dump(exclude={"id"})

    save_data(data)

    return JSONResponse(
        status_code=201,
        content={
            "message": f"Patient with ID {patient.id} created successfully"
        },
    )


@app.put("/update_patient/{patient_id}")
def update_patient(patient_id: str, patient_update: patient_update):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} not found"
        )
    existing_patient = data[patient_id]
    patient_data = patient_update.model_dump(exclude_unset=True)

    # Update the existing patient data with the new values
    data[patient_id].update(patient_data)
    for key, value in patient_data.items():
        existing_patient[key] = value

    patient_pydantic = Patient(id=patient_id, **existing_patient)
    existing_patient = patient_pydantic.model_dump(exclude={"id"})

    data[patient_id] = existing_patient

    save_data(data)

    return {
        "message": f"Patient with ID {patient_id} updated successfully"
    }


@app.delete("/delete_patient/{patient_id}")
def delete_patient(patient_id: str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} not found"
        )

    del data[patient_id]
    save_data(data)

    return {
        "message": f"Patient with ID {patient_id} deleted successfully"
    }