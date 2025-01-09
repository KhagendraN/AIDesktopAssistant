#app_password = "poes vbhb ecik cnsx"

import imaplib
import email
from email.header import decode_header

# Your email and app password
username = "your_email@gmail.com"
app_password = "poes vbhb ecik cnsx"

def list_emails():
    # Connect to the Gmail IMAP server
    imap = imaplib.IMAP4_SSL("imap.gmail.com")

    # Login to the account
    imap.login(username, app_password)

    # Select the mailbox you want to read (in this case, "INBOX")
    imap.select("INBOX")

    # Search for all emails in the INBOX
    status, messages = imap.search(None, "ALL")

    # Convert messages to a list of email IDs
    email_ids = messages[0].split()

    # Fetch the most recent email
    status, msg_data = imap.fetch(email_ids[-1], "(RFC822)")

    # Parse the email content
    msg = email.message_from_bytes(msg_data[0][1])
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")

    print(f"Subject: {subject}")

    # Close the connection and logout
    imap.close()
    imap.logout()
