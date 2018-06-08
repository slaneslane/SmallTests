import re

def validate_email(email):
    EMAIL_REGEXP = re.compile(r'^([\w.-]+)@([\w.-]+)$')
    return EMAIL_REGEXP.match(email)

email = 'slane@wp.pl'
if validate_email(email):
    print('email ok')
else:
    print('wrong email')
