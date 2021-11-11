import os
import logging

from logging.handlers import TimedRotatingFileHandler


class RollingCellLogger:

    def __init__(self, audit_dir="/opt/jupyterhub/audit", audit_file="audit.log", when="h", interval=1):

        # create audit directory if it doesn't exist yet
        if not os.path.exists(audit_dir):
            os.makedirs(audit_dir)

        path = os.path.join(audit_dir, audit_file)
        handler = TimedRotatingFileHandler(path, when=when, interval=interval)

        self._logger = logging.getLogger("RollingCellLogger")
        self._logger.addHandler(handler)

    def log(self, msg):
        self._logger.info(msg)