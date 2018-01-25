from flask import request


class CurlConnector(object):
    def __init__(self, bot):
        self.bot = bot
        self.bot.app.add_url_rule(
            '/' + 'webhook',
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
        response_message = self.bot.get_response(input_message)
        return self.send_message(response_message)
 
    def send_message(self, text):
        return text, 200

