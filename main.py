# import json
# from fastapi import FastAPI,Path,HTTPException,Query

# print("LOADING MY MAIN.PY")

# app = FastAPI()

# def load_data():
#     with open("patients.json", "r") as f:
#         data = json.load(f)
#         return data

# @app.get("/")
# def hello():
#     return {"message": "Patient Management System Api"}

# @app.get("/about")
# def about():
#     return {"message": "This is the about page for the Patient Management System."}

# @app.get("/view")
# def view():
#     data = load_data()
#     return data


# @app.get('/patient/{patient_id}')
# def get_patient(patient_id: str=Path(..., description="The ID of the patient to retrieve",example="P001")):
#     # Load the patient data from the JSON file
#     data = load_data()
#     # Search for the patient with the given ID
#     if patient_id in data:
#         return data[patient_id]
#     raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")

# @app.get('/sort')
# def sort_patients(sort_by: str=Query(..., description="Sort in basis of Height Weight or BMI "),order:str=Query('asc',description='Sort in Asc or Dsc order')):
#      valid_sort_fields = ['Height', 'Weight', 'BMI']
#      if sort_by not in valid_sort_fields:
#             raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid options are: {(valid_sort_fields)}")
#      if order not in ['asc', 'desc']:
#          raise HTTPException(status_code=400, detail="Invalid order. Valid options are: 'asc' or 'desc'")
#      data = load_data()
     
#      sorted_data=sorted(data.values(),key=lambda x: x.get(sort_by, 0),reverse=False)
#      return sorted_data
                                







import json
from fastapi import FastAPI, Path, HTTPException, Query

print("LOADING MY MAIN.PY")

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        return json.load(f)

@app.get("/")
def hello():
    return {"message": "Patient Management System Api"}

@app.get("/about")
def about():
    return {"message": "This is the about page for the Patient Management System."}

@app.get("/view")
def view():
    return load_data()

@app.get("/patient/{patient_id}")
def get_patient(
    patient_id: str = Path(..., description="The ID of the patient to retrieve", examples={"example": "P001"})
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on basis of Height, Weight, or BMI"),
    order: str = Query("asc", description="Sort order: asc or desc")
):
    valid_sort_fields = ["Height", "Weight", "BMI"]

    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid options: {valid_sort_fields}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Use 'asc' or 'desc'")

    data = load_data()

    reverse = True if order == "desc" else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse
    )

    return sorted_data