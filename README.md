# jupyter-audit
A Jupyter server extension for auditing code run in notebooks.

Install the server extension
`/opt/jupyterhub/bin/python3 -m pip install -e .`

Enable the server extension
`jupyter serverextension enable --py jupyter-audit`

Start JupyterHub
`/opt/jupyterhub/bin/jupyterhub -f /opt/jupyterhub/etc/jupyterhub/jupyterhub_config.py`
