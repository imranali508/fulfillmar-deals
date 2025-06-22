# -*- coding: utf-8 -*-

from subscribers import UNSUBSCRIBE_SHEET_ID, get_sheet_emails

def main():
    try:
        emails = get_sheet_emails(UNSUBSCRIBE_SHEET_ID)
        print(f"✅ Unsubscribe-sheet emails ({len(emails)}):")
        for e in sorted(emails):
            print("  ", e)
    except Exception as e:
        print("❌ ERROR fetching unsubscribe sheet:", e)

if __name__ == "__main__":
    main()
