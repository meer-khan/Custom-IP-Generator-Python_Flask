# Custom IP Generator - Python Flask

![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Flask Version](https://img.shields.io/badge/Flask-2.0%2B-blue)

Custom IP Generator is a Python Flask application that allows you to access custom IP addresses sent from a client. This application serves as a simple example of a server-client interaction, where the Flask server receives custom IP addresses from the client and processes them.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you start, make sure you have the following installed:

- Python 3.8 or higher
- Flask 2.0 or higher

You can install Flask using pip:

```bash
pip install Flask
```

## Getting Started
1. Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/Custom-IP-Generator-Python_Flask.git
```

2. Change to the project directory:
```bash
cd Custom-IP-Generator-Python_Flask
```

3. Run the Flask application:
```bash
python app.py
```
Your Flask application should now be running locally.  

## Usage  
Once the application is running, you can access it at http://localhost:5000.   Now you can send a request to the server using ```client.py``` file.

## API Endpoints
The following API endpoints are available:

- /IPgetter/: POST custom IP addresses to the server.   
You can interact with these endpoints to send and retrieve custom IP addresses.

