# Custom IP Generator - Python Flask [![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Follow me on Medium](https://img.shields.io/badge/Medium-%40meer--khan-02b875?style=for-the-badge&logo=medium)](https://medium.com/@meer-khan) [![GitHub](https://img.shields.io/badge/GitHub-%40meer--khan-181717?style=for-the-badge&logo=github)](https://github.com/meer-khan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%40meer--khan-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/meer-khan/)

![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Flask Version](https://img.shields.io/badge/Flask-2.0%2B-blue)


Custom IP Generator is a Python Flask application that allows you to access custom IP addresses sent from a client. This application serves as a simple example of a server-client interaction, where the Flask server receives custom IP addresses from the client and processes them.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running the Client File](#running-the-client-file)
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

## Running the Client File

The client file allows you to send custom IP addresses to the Flask server. Follow these steps to run the client file:

1. Ensure that you have Python 3.x installed on your local machine.  
2. Open the client file in a text editor or Python IDE of your choice.  
3. Locate the `custom_ip` variable in the client file. It is the variable that holds the custom IP address you want to send to the server.  
4. Modify the `custom_ip` variable to the desired IP address you want to send. For example:  
   ```python
   custom_ip = "192.168.1.100"
5. Save the File  
5. Open the Terminal, navigate to client file and run  
   ```bash
   python client.py

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

- Fork the repository.  
- Create a new branch for your feature:
    - git checkout -b feature-name.
- Make your changes and commit them:
    - git commit -m 'Add some feature'.
- Push to your branch: git push origin feature-name.
- Submit a pull request with a description of your changes.  

## License
This project is licensed under the MIT License - see the LICENSE file for details.

