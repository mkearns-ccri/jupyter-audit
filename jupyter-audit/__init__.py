import json

from .logger import RollingCellLogger


def _jupyter_server_extension_paths():
    return [{
        "module": "jupyter-audit"
    }]

def load_jupyter_server_extension(nb_server_app):

    from notebook.services.kernels.handlers import ZMQChannelsHandler

    logger = RollingCellLogger()

    _old =  ZMQChannelsHandler.on_message

    def _new(*args, **kwargs):

        self = args[0]
        msg = json.loads(args[1])
        msg_type = msg['header']['msg_type']

        if msg_type == 'execute_request':
            logger.log({
                'username': self.get_current_user()['name'],
                'session': msg['header']['session'],
                'cell_id': msg['metadata']['cellId'],
                'message_id': msg['header']['msg_id'],
                'message_type': msg_type,
                'datetime': msg['header']['date'],
                'code': msg['content']['code'],
            })

        return _old(*args, **kwargs)

    ZMQChannelsHandler.on_message = _new