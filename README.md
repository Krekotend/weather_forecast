
# Weather Forecast Django Project

This is a Django project that provides weather forecasts for cities. The application allows users to search for weather forecasts, view current weather conditions, and track search history.

On assignment:
- tests written
- when visiting the site again, you will be asked to view the situation in the city in which the user has previously looked.
Implemented using session saves
- the definition history for each user will be saved, and there will be an API indicating how many times which city was entered
Saved with the database. Can be viewed through the admin panel or [API](http://127.0.0.1:8000/api/city_search_counts/) 
```examp
YOUR_DOMEN/api/city_search_counts/
```


## Installation

### Prerequisites

- Python 3.10 or higher
- `pip` (Python package installer)
- Virtual environment tool (optional but recommended)

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/weather_forecast.git
cd weather_forecast
```

### Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python -m venv env
```

Activate the virtual environment:

- On Windows:

```bash
env\Scripts\activate
```

- On macOS and Linux:

```bash
source env/bin/activate
```

### Install Dependencies

Install the required libraries:

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

Run the following commands to apply database migrations:

```bash
python manage.py migrate
```

### Create a Superuser Account

Create a superuser account for accessing the Django admin interface:

```bash
python manage.py createsuperuser
```

### Configure API Key for Weather Forecast

Register on [WeatherAPI](https://www.weatherapi.com) and get an API key. Save it in a `.env` file with the variable name `TOKEN`:

```env
TOKEN=your_api_key_here
```

### Running the Application

Start the development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your web browser to view the application.

### Access the Admin Interface

Navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with the superuser account you created.

## Testing

To run tests, execute:

```bash
python manage.py test
```
