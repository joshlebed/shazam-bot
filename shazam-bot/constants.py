"""contains constants used across modules"""

import logging

# --- global ---
# in prod, run with logging level critial -
#   this hides all of our exception handling, and only allows print statements
# LOGGING_LEVEL = logging.CRITICAL
# in dev, run with logging level info or warn
# LOGGING_LEVEL = logging.WARN
LOGGING_LEVEL = logging.INFO
