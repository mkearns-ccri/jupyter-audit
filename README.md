# jupyter-audit

A Jupyter server extension for auditing code run in notebooks.

## Installation

1. Clone the repository `git clone git@github.com:mkearns-ccri/jupyter-audit.git`

2. Move into the directory `cd /your/path/to/jupyter-audit`

3. Install the server extension `/opt/jupyterhub/bin/python3 -m pip install -e .`

4. Enable the server extension `/opt/jupyterhub/bin/jupyter serverextension enable --py jupyter-audit --sys-prefix`

5. Start JupyterHub `/opt/jupyterhub/bin/jupyterhub -f /opt/jupyterhub/etc/jupyterhub/jupyterhub_config.py`

## Configuring the Logger

By default, the logger is configured to log information to `/opt/jupyterhub/audit`. If this directory does not exist when the logger is initialized, it will be created by the logger. The default logging destination can be changed in `logger.py` or configured as an argument used to initialize the logger in `__init__.py`.

The logger is a `TimedRotatingFileHandler` which means that log snapshots will be taken at discrete time intervals, which helps ensure that the log files will not grow too large. Currently, log snapshots will be taken *once per hour*. The default time intervals can be configured either in `logger.py` or passed as an argument to the logger constructor in `__init__.py`.

Examples: 

`when = 'm', interval = 30` implies a time interval of 30 minutes, and `when = 'h', interval = 10` implies a time interval of 10 hours.

### Configurable Parameters

1. `audit_dir` is the directory to hold the audit logs.
2. `audit_file` is the name of the open audit log.
3. `when` is the log snapshot frequency `m` = minutes, `h` = hours, and `d` = days.
4. `interval` is the number of seconds, minutes, hours, or days.


