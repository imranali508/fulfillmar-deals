# -*- coding: utf-8 -*-

from subscribers import SIGNUP_SHEET_ID, get_sheet_emails

def main():
    try:
        emails = get_sheet_emails(SIGNUP_SHEET_ID)
        print(f"✅ Signup-sheet emails ({len(emails)}):")
        for e in sorted(emails):
            print("  ", e)
    except Exception as e:
        print("❌ ERROR fetching signup sheet:", e)

if __name__ == "__main__":
    main()
