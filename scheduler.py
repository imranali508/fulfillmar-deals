# scheduler.py

from scraper import scrape_all
from mailer  import send_deals_email

def main():
    deals = scrape_all()
    send_deals_email(deals)

if __name__ == "__main__":
    main()
