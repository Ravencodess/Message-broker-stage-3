# Messaging System

A FastAPI-based messaging system with Celery task queue integration for sending emails. The system logs actions and exposes an API to trigger tasks and view logs.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Usage](#api-usage)
- [Logging](#logging)
- [Contributing](#contributing)

## Features

- **API Endpoints:**
  - `/`: Main endpoint to trigger sending emails and logging messages.
  - `/logs`: Endpoint to retrieve log contents.
- **Task Queue:** Uses Celery with RabbitMQ as the broker.
- **Email Sending:** Utilizes SMTP to send emails.

## Project Structure
```
    .
    ├── app
    │   ├── Main.py
    │   └── Tasks.py
    └── requirements.txt
```

## Getting Started

### Prerequisites

- **Python 3.8+**
- **RabbitMQ Server**
- **SMTP Email Account**

### Installation

1. **Clone the repository:**
```
    git clone https://github.com/Ravencodess/message-broker-stage-3
    cd message-broker-stage-3
```
2. **Create and activate a virtual environment:**
```
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
```
3. **Install dependencies:**
```
    pip install -r requirements.txt
```
4. **Set up environment variables:**

    Create a `.env` file in the project root and add the following:
```
    email_sender=your_email@example.com
    email_password=your_email_password
```
5. **Run RabbitMQ server:**

    Ensure RabbitMQ is running on `localhost:5672`.

### Running the Application

1. **Start the FastAPI application:**
```
    uvicorn app.Main:app --reload
```
2. **Start the Celery worker:**
```
    celery -A app.Tasks worker --loglevel=info
```
## API Usage

- **Trigger Email Sending and Logging:**
```
    GET /?sendmail=recipient@example.com&talktome=Your+message
```
- **Retrieve Logs:**
```
    GET /logs
```
## Logging

- **Log File:** The system logs are stored in `/var/log/messaging_system.log`.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.