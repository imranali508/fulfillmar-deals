# mailer.py

import os
import random
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# ----------------- CONFIG -----------------
FROM_EMAIL = os.getenv("FROM_EMAIL", "deals@fulfillmar.com")
TO_EMAIL   = os.getenv("TO_EMAIL", "")
# ------------------------------------------

# Define your subject‐line templates, using {date} placeholder
SUBJECT_TEMPLATES = [
    "🔥 {date} FulfillMar Hot Deals—Grab ’Em Before They’re Gone!",
    "🚀 Today’s Top Deals ({date}) from FulfillMar",
    "🎯 {date}: Your Curated FulfillMar Deals Are Here",
    "✨ FulfillMar Deals {date} | Limited-Time Savings Inside"
]

def send_deals_email(deals):
    """Send an HTML email of deals via SendGrid, with a random subject."""
    if not deals:
        print("No deals to send.")
        return

    # Format date as MM-DD-YY
    date_str = datetime.now().strftime("%m-%d-%y")
    # Pick one of the subjects at random:
    subject = random.choice(SUBJECT_TEMPLATES).format(date=date_str)

    # Build HTML body with timestamp
    now = datetime.now().strftime("%m-%d-%y %I:%M %p")
    html = f"<h2>🔥 FulfillMar Deals @ {now} 🔥</h2><ul>"
    for d in deals:
        html += (
            f"<li>"
            f"<a href='{d['url']}'>{d['title']}</a> — <strong>{d['price']}</strong>"
            f"</li>"
        )
    html += "</ul>"

    # Append unsubscribe link
    html += (
        "<p style='font-size:small;color:gray;'>"
        "To unsubscribe, please click "
        "<a href='https://docs.google.com/forms/d/1gBNw8iZfI4L4QLWyK1hjQcyEbNxlpMr2pYOTFWrf4yI/viewform?edit_requested=true'>here</a>."
        "</p>"
    )

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL.split(","),  # can be comma-separated
        subject=subject,
        html_content=html
    )

    try:
        sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])
        resp = sg.send(message)
        print(f"✅ Email sent! Status code: {resp.status_code}")
    except Exception as e:
        print("❌ Failed to send email:", e)

if __name__ == "__main__":
    # local smoke-test
    from scraper import scrape_all
    deals = scrape_all()
    send_deals_email(deals)
