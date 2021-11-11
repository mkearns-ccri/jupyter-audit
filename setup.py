import setuptools

setuptools.setup(
    name="jupyter-audit",
    include_package_data=True,
    data_files=[
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/jupyter-audit.json"
        ])
    ],
    zip_safe=False
)