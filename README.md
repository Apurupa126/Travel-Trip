# Travel-Trip
My travel planning platform that provides users with information on hotels, restaurants, and local services at their chosen destination. Built to simplify travel planning and enhance user experience.
# Travel Trip - Smart Travel Assistant

## Overview

Travel Trip is a smart travel planning web application developed using Django. It helps users plan trips efficiently by providing hotel recommendations, restaurant suggestions, weather updates, nearby hospitals, police stations, popular tourist attractions, route guidance, budget estimation, and an interactive travel chatbot.

The platform aims to simplify travel planning by offering essential travel information in a single application.

---

## Features

* User Registration and Login
* Hotel Recommendations
* Restaurant Recommendations
* Weather Information
* Popular Tourist Places
* Route and Direction Assistance
* Budget Planning
* Nearby Hospitals
* Nearby Police Stations
* Interactive Travel Chatbot
* User-Friendly Interface

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Django

### Database

* SQLite

---

## Project Structure

```text
smarttravel/
│
├── manage.py
│
├── smarttravel/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── travelapp/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
└── templates/
    ├── home.html
    ├── login.html
    ├── register.html
    ├── hotels.html
    ├── restaurants.html
    ├── weather.html
    ├── hospitals.html
    ├── policestations.html
    ├── popularplaces.html
    ├── directions.html
    ├── budget.html
    ├── result.html
    └── travel_chatbot.html
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Apurupa126/Travel-Trip.git
cd Travel-Trip
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install django
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

### Open Browser

```text
http://127.0.0.1:8000/
```

---

## Use Cases

* Trip Planning
* Tourist Guidance
* Budget Management
* Weather Monitoring
* Travel Safety Support
* Local Service Discovery

---

## Future Enhancements

* AI-Based Personalized Travel Recommendations
* Real-Time Traffic Updates
* Hotel and Flight Booking Integration
* Multi-Language Support
* Voice Assistant Integration
* GPS-Based Live Navigation

---

## Author

**Apurupa**

GitHub: https://github.com/Apurupa126

---

## License

This project is licensed under the MIT License.

