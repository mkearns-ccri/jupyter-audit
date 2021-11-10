def _jupyter_server_extension_paths():
    return [{
        "module": "jupyter-audit"
    }]

def load_jupyter_server_extension(nb_server_app):
    from jupyter_server.services.kernels.handlers import ZMQChannelsHandler
    with open('/home/mkearns/hello.txt', 'w') as ofile:
        ofile.write("This worked?")
    _old =  ZMQChannelsHandler.on_message
    def _new(*args, **kwargs):
      with open('/home/mkearns/audit.txt', 'w') as ofile:
          ofile.write("This worked!")
      return _old(*args, **kwargs)
    ZMQChannelsHandler.on_message = _new