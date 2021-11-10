import setuptools

setuptools.setup(
    name="jupyter-audit",
    
    include_package_data=True,
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        # ("share/jupyter/nbextensions/audit", [
        #     "my_fancy_module/static/index.js",
        # ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/notebook.d", [
            "jupyter-config/nbconfig/notebook.d/jupyter-audit.json"
        ]),
        # like `jupyter serverextension enable --sys-prefix`
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/jupyter-audit.json"
        ])
    ],
    
    zip_safe=False
)