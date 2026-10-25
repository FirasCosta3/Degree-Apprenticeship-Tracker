# Degree Apprenticeship Tracker

Automated Python web scraper and Flask dashboard built to help you track Technology Degree Apprenticeships live
Building this project has allowed me to apply early to the degree apprenticeships that the scraper has found, running it on `GitHub Actions` every 4 hours.

## What it does
* **Automated Web Scraping:** Extracts live job data from safe scraper friendly career sites.
* **Email Alerts:** Sends email notifications when new roles are detected (via Github automation).
* **Interactive Dashboard:** A Flask web interface using JavaScript's POST method and Jinja to handle backend data and a user interface.
* **Job Searches:** You can chose up to 7 different job titles to search for, changing it based on user preference
* **Job Management:** You are able to remove jobs you dont want moving it to the `bin` page where you can restore back to home.
* **Application Tracking:** Each job listing has a dedicated checkmark button you can press when you have applied to the job, sending it to the bottom of the page and adding +1 to the applied to tally at the top.
* **Data Handling:** SQLite to store active jobs and track users removed jobs, used a JSON file that the Github agent appends after each new job so no duplicate emails are sent.

## Tech Stack
* **Backend:** Python, Flask
* **Database:** SQLite
* **Frontend:** HTML, CSS, JavaScript

## Local Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Firas12123/Degree-Apprenticeship-Finder.git
   ```

2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run Locally
   ```bash
   python3 main.py
   ```