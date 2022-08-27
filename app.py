from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from summarize import summarize_prompt


app = Flask(__name__)


def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)


@app.route("/summary", methods=['GET', 'POST'])
def incoming_sms():
    user_input = request.form.get('NumMedia')
    if user_input == '1':
        pic_url = request.form.get('MediaUrl0')
        summary = summarize_prompt(pic_url)
        return respond(f"{summary}")
    else:
        return respond(f"Please send a picture containing text!")


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=8080)
