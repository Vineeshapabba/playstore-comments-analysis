from flask import Flask,render_template,request
import joblib
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pandas

clf=joblib.load("vinny.pkl")


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    if request.method == "POST":
        s = request.form["pandu"]
        ans=clf.predict([s])
        if ans == [1] or [2] or [3]:
            from twilio.rest import Client

            account_sid = 'ACd811fb3b57f1c766a9dfdc27cfa9a8a7'
            auth_token = 'fbd7118a7dcd324775be59ff6986cfe5'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_='+16185563697',
            body=s,
            to='+916302083849'
            )

            print(message.sid)

            from twilio.rest import Client

            # Your Twilio Account SID and Auth Token
            account_sid = "ACd811fb3b57f1c766a9dfdc27cfa9a8a7"
            auth_token = "fbd7118a7dcd324775be59ff6986cfe5"

            # Create a Twilio client
            client = Client(account_sid, auth_token)

            # The phone number you want to call
            to_number = "+916302083849"  # Replace with the recipient's number

            # The Twilio phone number making the call
            from_number = "+16185563697"  # Replace with your Twilio phone number

            # The message you want to say during the call
            message = s

            # Make the call
            call = client.calls.create(
                to=to_number,
                from_=from_number,
                twiml=f"<Response><Say>{message}</Say></Response>",
            )

            print(f"Call SID: {call.sid}")

            print(f"Call SID: {call.sid}")
        return render_template("index.html",score=ans)
    return render_template("index.html")

if __name__== "__main__":
    app.run()