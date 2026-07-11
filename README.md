# 🏥 Patient Management System API

A RESTful **Patient Management System API** built with **FastAPI** and **Pydantic**. This project demonstrates how to build a scalable backend API with complete CRUD operations, request validation, automatic BMI calculation, and interactive API documentation.

---

# 🚀 Features

* ➕ Create a new patient
* 📋 View all patients
* 🔍 Retrieve a patient by ID
* ✏️ Update patient information
* ❌ Delete a patient
* 📊 Sort patients by Height, Weight, or BMI
* 🧮 Automatic BMI calculation
* 💡 Automatic BMI health verdict
* ✅ Request validation using Pydantic
* ⚠️ Proper exception handling
* 📖 Interactive API documentation with Swagger UI

---

# 🛠️ Tech Stack

* Python
* FastAPI
* Pydantic v2
* Uvicorn
* JSON (Data Storage)

---

# 📂 Project Structure

```text
Patient-Management-System/
│── main.py
│── patients.json
│── requirements.txt
│── README.md
└── .gitignore
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-github-username>/Patient-Management-System.git
```

### Move into the project directory

```bash
cd Patient-Management-System
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the server

```bash
uvicorn main:app --reload
```

Server will run on:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 📌 API Endpoints

| Method | Endpoint                         | Description       |
| ------ | -------------------------------- | ----------------- |
| GET    | `/`                              | Home              |
| GET    | `/about`                         | About the API     |
| GET    | `/view`                          | View all patients |
| GET    | `/patient/{patient_id}`          | Get patient by ID |
| GET    | `/sort?sort_by=Height&order=asc` | Sort patients     |
| POST   | `/create_patient`                | Create a patient  |
| PUT    | `/update_patient/{patient_id}`   | Update patient    |
| DELETE | `/delete_patient/{patient_id}`   | Delete patient    |

---

# 🧮 BMI Calculation

The API automatically calculates the Body Mass Index (BMI):

```text
BMI = Weight (kg) / Height² (m²)
```

Based on the BMI value, the API also returns a health verdict:

* Underweight
* Normal Weight
* Overweight
* Obesity

---

# 📚 Concepts Practiced

* REST API Development
* CRUD Operations
* FastAPI Routing
* Pydantic Models
* Data Validation
* Computed Fields
* Query Parameters
* Path Parameters
* HTTP Status Codes
* Exception Handling
* JSON Responses
* File Handling
* API Documentation

---

# 📸 Screenshots

Add screenshots of your API here:

* Swagger UI Home
* Create Patient
* View Patient
* Update Patient
* Delete Patient
* Sort Patients

---

# 🚀 Future Improvements

* MongoDB Integration
* PostgreSQL Support
* JWT Authentication
* User Login & Registration
* Search & Filtering
* Pagination
* Docker Support
* Unit Testing with Pytest
* Deployment on Render/Railway
* CI/CD using GitHub Actions

---

# 🎯 Learning Outcome

This project helped me strengthen my understanding of:

* Backend development using FastAPI
* Building RESTful APIs
* Data validation with Pydantic
* Request and response handling
* Clean API design
* Error handling
* API documentation with Swagger UI

It also serves as a strong foundation for deploying AI/ML models using FastAPI in future projects.

---

# 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

If you'd like to improve this project, feel free to fork the repository and submit a pull request.

---

# ⭐ Show Your Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀
