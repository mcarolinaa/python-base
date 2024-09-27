#!/usr/bin/env python3

import os
import logging
from logging import handlers


# boilerplate
# todo: make function
# todo: use external lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# our instance - default: only shows from warning up (error and critical)
log = logging.Logger(__name__, log_level) # debug or 10
# ch = logging.StreamHandler() # handler: write in my destination of choice
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log",
    maxBytes=300, # recommended = 10**6
    backupCount=10 # num of backup files
    )
fh.setLevel(log_level)
fmt = logging.Formatter(    # formating
    '%(asctime)s %(name)s %(levelname)s'
    'l:%(lineno)d f:%(filename)s %(message)s'
)
# ch.setFormatter(fmt)
# log.addHandler(ch)
fh.setFormatter(fmt)
log.addHandler(fh)

# what can be adjusted when using the logging module: (above)
# level
# format 
# destination

"""
# uses the instance, if you change anything from default 
log.debug("Message to developer, qe, sysadmin")
log.info("General message to user, low importance")
log.warning("Warning that does not cause error")
log.error("Error affecting one execution")
log.critical ("General error that affects all")
"""

print("---")

try:
    1/0
except ZeroDivisionError as e:
    log.error("[ERROR] Error %s", str(e))
    