from gevent.wsgi import WSGIServer
from chatterbot import ChatBot
from chatterbot.utils.module_loading import import_module
from flask import Flask


class FlaskChatBot(ChatBot):
    def __init__(self, name, **kwargs):
        kwargs['input_adapter'] = (
            'chatterbot.adapters.input.VariableInputTypeAdapter')
        kwargs['output_adapter'] = (
            'chatterbot.adapters.output.OutputFormatAdapter')
        kwargs['output_format'] = 'text'
        connector_name = kwargs.get(
            'connector',
            'connectors.CurlConnector'
        )
        super(FlaskChatBot, self).__init__(name, **kwargs)
        self.host = kwargs.get(
            "host",
            "127.0.0.1"
        )
        self.port = kwargs.get(
            "port",
            5000
        )
        self.app = Flask(__name__)
        ConnectorClass = import_module(connector_name)
        self.connector = ConnectorClass(self)

    def run(self):
        http_server = WSGIServer((self.host, self.port), self.app)
        http_server.serve_forever()
