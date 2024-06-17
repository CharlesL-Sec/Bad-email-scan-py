# Bad-email-scanner-py

### Extracts emails addresses from a user provide list and check for MX records.  Those emails addresses without an MX record can be considered not active 

#### Using Python 3.11
##### smtp, urllib

This python script will scan 1000's of email addresses to check for a DNS MX record.
If the MX record does not exist, the email address can be considered no longer active.

Uses python threads for rapid list inspection and rapid requests.



