# FinancialTracker
CPSC 362: Software Engineer Project - FinancialTracker is a financial analysis tool that implements a web scraper to crawl the Yahoo Finance API. The data is then stored in our own Django REST API to be used for visualization and algorithmic predictions of the individual stocks. The final product will be a web application with frontend in HTML5, CSS3, and Vue.js using the Vuetify Framework requesting to our backend Django API. 

## Getting Started

First, to get started on deployment you must clone the github repository. Go to the desired directory to place the project and clone the repository in a Git Bash terminal using the command 'git clone https://github.com/Abeeaad97/FinancialTracker.git. After doing so, enter in to the project directory and follow steps under "Installing".

### Prerequisites

To run the application you will need the latest version of Node.js and npm installed along with Python to install the following:

Windows 10 
```
python -m install -U pip
pip install django
pip install djangorestframework
pip install django-filter
```

### Installing

A step by step guide to run the local host frontend and backend servers:

Locate the project directory using a Linux terminal or Git Bash. Then set your current directory to the frontend folder to run the command 'npm install' to install dependencies. After doing so, in the same directory run 'npm run serve' and a local server should start up on http://localhost:8080. Next, open another separate terminal and locate the backend directory. When found, run the following command 'python manage.py runserver' and the default local server is on http://localhost:8000/admin. In order to login to the Django API you have to create a superuser by the command 'python manage.py createsuperuser' (may require 'winpty python manage.py createsuperuser' on Windows). Both servers should be locally running on the default ports mentioned. Ideally, the servers will be hosted on the cloud using AWS S3 Bucket frontend and EC2 Instance backend.

Windows 10
```
cd C:/Users/username/Documents/FinancialTracker
cd frontend
npm install
npm run serve


In a separate terminal:
cd C:/Users/username/Documents/FinancialTracker
cd backend
winpty python manage.py createsuperuser
python manage.py runserver
```

## Running the tests

In the project main directory, locate the spiders folder and stocks.py Python script. This is where we temporarily test the scraper and loading it to the database. Run the following command and the data can be found in the Django UI.

```
python stocks.py
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Vue](https://vuejs.org/v2/guide/) - A progressive javascript framework for user interface
* [Vuetify](https://vuetifyjs.com/en/getting-started/quick-start/) - Material design component framework for a clean frontend
* [Axios](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis/) - Promise based HTTP client for frontend to request backend
* [Django](https://docs.djangoproject.com/en/3.0/) - The database web framework
* [Django REST Framework](https://www.django-rest-framework.org/) - The Rest framework to assist making our API
* [Python 3](https://docs.python.org/3/) - The language used for our backend and web scraper
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library to assist web scraping


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.
 

## Authors

* **Tyler Bloom** - (https://github.com/Tbloom9787)
* **Abid Bakhtiyar** = (https://github.com/Abeeaad97)
* **Jordan Wermuth** - (https://github.com/JordanWermuth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
