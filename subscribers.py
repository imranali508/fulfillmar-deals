# subscribers.py

import gspread
from google.oauth2.service_account import Credentials

# IDs from the URLs of each form’s response spreadsheet
SIGNUP_SHEET_ID      = "18UDjM6boAtcNqXBMgHswpRoR208DXQUV01KaxiJk7TQ"
UNSUBSCRIBE_SHEET_ID = "1J9qpyCobkvjWBtRTZp3wgOdKLR5fvqeiDe-rko_SG2U"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def get_sheet_emails(sheet_id, col=2):
    creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
    gc = gspread.authorize(creds)
    ws = gc.open_by_key(sheet_id).sheet1
    # skip header, grab column B (emails)
    return set(ws.col_values(col)[1:])

def get_subscribers():
    all_subs = get_sheet_emails(SIGNUP_SHEET_ID)
    unsub   = get_sheet_emails(UNSUBSCRIBE_SHEET_ID)
    # Return only those who signed up and haven’t unsubscribed
    return sorted(all_subs - unsub)

if __name__ == "__main__":
    print("Active subscribers:", get_subscribers())
