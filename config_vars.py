"""
Part 1 of the config job - configuring the innards of the app.
"""

__author__ = 'donal'
__project__ = 'ribcage'

import os
import re

# ====================
# POPULATE POSTGRES_KEYS AND #1-3 BLANKS AS REQUIRED
# ====================
DBNAME = 'ribcage'
PK = os.environ.get('POSTGRES_KEYS', 'BLANK BLANK').split()
# links db_models.py and forms.py -
MAX_COL_WIDTHS = 30
MIN_PASS_LEN = 6
ADMIN_USER = False
INITIALLY_ACTIVE = True
# first users under db_init -
RIBCAGE_KEY01 = os.environ.get('RIBCAGE_ADMIN_KEYS1', 'BLANK BLANK').split()
RIBCAGE_KEY02 = os.environ.get('RIBCAGE_ADMIN_KEYS2', 'BLANK BLANK').split()

# ====================
# CLIENT IP HANDLING
# ====================
VALID_IP = re.compile(r"""
\b
(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
\b
""", re.VERBOSE)

# ====================
# NAME OF YOUR LOG FILE
# ====================
LOGOUT = 'Devel_logs.log'

# ====================
# MAILGUN VARIABLES
# ====================
MAILGUN_URL = 'https://api.mailgun.net/v3/{}/messages'
SANDBOX = 'sandbox26a6aabbd3e946feba81293c4b4d9dcc.mailgun.org'
MAILGUN_KEY = os.environ.get('MAILGUN_KEY')

# ====================
# AWS VARIABLES
# ====================
AWS_KEYS = os.environ.get('AWS_KEYS')
if AWS_KEYS is not None: tmp = AWS_KEYS.split(' ')
else: tmp = [None, None]
AWS_KEYS = {
    'S3_KEY': tmp[0],
    'S3_SECRET': tmp[1]
}

# ====================
# MAP VARIABLES
# ====================
GOOGLE_MAP_KEY = os.environ.get('GOOGLE_MAP_KEY', 'BLANK')
GOOGLE_MAP_KEY = 'AIzaSyCUUQ2wiXcK1ujPsk25QAd6aAgLjhcdpUM'
MAP_URL = 'https://maps.googleapis.com/maps/api/js?key={}'.format(GOOGLE_MAP_KEY)


# ========================
if __name__ == '__main__':
    print PK
    print AWS_KEYS
