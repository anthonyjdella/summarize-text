from flask import Flask, request
# Import MessagingResponse class
from summarize import summarize_prompt


app = Flask(__name__)

# Create respond()

@app.route("/summary", methods=['GET', 'POST'])
def incoming_sms():
    user_input = request.form.get('NumMedia')
    if user_input == '1':
        pic_url = request.form.get('MediaUrl0')
        summary = summarize_prompt(pic_url)
        return respond(f"{summary}")
    else:
        return respond("Please send a picture containing text!")


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=8080)
