# -*- coding: utf-8 -*-

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Instantiate client using the SENDGRID_API_KEY environment variable
sg = SendGridAPIClient(os.environ["SENDGRID_API_KEY"])

# Build a simple test message
message = Mail(
    from_email="deals@fulfillmar.com",
    to_emails="you@yourdomain.com",   # replace with your address
    subject="SendGrid Auth Test",
    html_content="<p>If you receive this, your API key and sender domain are correctly configured!</p>"
)

# Send and print status
resp = sg.send(message)
print(f"Status: {resp.status_code}")
