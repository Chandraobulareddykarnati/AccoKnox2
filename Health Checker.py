import requests
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='application_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Application configuration
APP_URL = "http://your-application-url.com"  # Replace with the application's URL
TIMEOUT = 5  # Timeout for the HTTP request (in seconds)

def check_application_health():
    """Checks the health of the application by its HTTP response status."""
    try:
        response = requests.get(APP_URL, timeout=TIMEOUT)
        status_code = response.status_code

        if 200 <= status_code < 300:
            logging.info(f"Application is UP. Status code: {status_code}")
            print(f"Application is UP. Status code: {status_code}")
        else:
            logging.warning(f"Application is DOWN. Status code: {status_code}")
            print(f"Application is DOWN. Status code: {status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is DOWN. Error: {e}")
        print(f"Application is DOWN. Error: {e}")

if __name__ == "__main__":
    check_application_health()
