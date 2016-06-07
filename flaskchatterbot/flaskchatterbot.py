from chatterbot import ChatBot
from flask import Flask, request


class FlaskChatBot(ChatBot):
    def __init__(self, name, **kwargs):
        kwargs['input_adapter'] = (
            'chatterbot.adapters.input.VariableInputTypeAdapter')
        kwargs['output_adapter'] = (
            'chatterbot.adapters.output.OutputFormatAdapter')
        kwargs['output_format'] = 'text'
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
        self.app.add_url_rule(
            '/' + name,
            'receive_call',
            self.receive_call,
            methods=['GET', 'POST']
        )

    def receive_call(self):
        if request.method == 'POST':
            return self.receive_message()
        else:
            return 'received get call', 200

    def receive_message(self):
        input_message = request.data
        response_message = self.get_response(input_message)
        return self.send_message(response_message)

    def send_message(self, text):
        return 'message sent ' + text, 200

    def run(self):
        self.app.run(host=self.host, port=self.port)
