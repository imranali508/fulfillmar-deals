# mailer.py

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import datetime

def send_deals_email(deals):
    """Send an HTML email of deals via SendGrid."""
    if not deals:
        print("No deals to send.")
        return

    # Build simple HTML body with timestamp
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    html = f"<h2>🔥 FulfillMar Deals @ {now} 🔥</h2><ul>"
    for d in deals:
        html += (
            f"<li>"
            f"<a href='{d['url']}'>{d['title']}</a> — <strong>{d['price']}</strong>"
            f"</li>"
        )
    html += "</ul>"

    # Read env vars (with sane defaults)
    from_email = os.getenv("FROM_EMAIL", "deals@fulfillmar.com")
    to_emails = os.getenv("TO_EMAIL", "support@fulfillmar.com")  # comma-sep list OK
    api_key   = os.getenv("SENDGRID_API_KEY")

    if not api_key:
        print("❌ SENDGRID_API_KEY not set in environment!")
        return

    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=f"FulfillMar Deals – {now}",
        html_content=html
    )

    try:
        sg = SendGridAPIClient(api_key)
        resp = sg.send(message)
        print(f"✅ Email sent! Status code: {resp.status_code}")
    except Exception as e:
        print("❌ Failed to send email:", e)


if __name__ == "__main__":
    # local smoke-test
    from scraper import scrape_all
    deals = scrape_all()
    send_deals_email(deals)
