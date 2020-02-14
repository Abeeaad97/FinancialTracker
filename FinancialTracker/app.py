import shutil
import schedule
import time
import subprocess

# Where data will be stored or removed
DATA_DIR = "../data/"

class Scraper():
    def __init__(self):
        pass

    def scrape_all(self):
        pass

    # Remove data file using shutil module
    def clean_all(self):
        shutil.rmtree(DATA_DIR, ignore_errors=True)


# Runs bash script to create environment
def job(app):
    app.scrape_all()

def main():
    app = Scraper()
    job(app)

    # Schedule to run at 8:00 a.m. every day
    schedule.every().day.at("08:00").do(job, app)

    # Sleep in between scraping
    while True:
        schedule.run_pending()
        time.sleep(100)

if __name__ == '__main__':
    main()
