from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Render a HTML form for input
    return render_template('form.html')

@app.route('/send', methods=['POST'])
def send():

    receiver_account_number = request.form.get('receiver_account_number')
    sender_account_number = request.form.get('sender_account_number')
    amount = request.form.get('amount')

    print(receiver_account_number, sender_account_number, amount)

    # Prepare JSON payload
    payload = {
        'receiver_account_number': receiver_account_number,
        'sender_account_number': sender_account_number,
        'amount': float(amount) if amount else None
    }

    # Send the JSON payload to the specified URL
    response = requests.get('http://127.0.0.1:8005/gateway', params=payload)

    # Check the response status code
    if response.status_code == 200:
        # If success, render a success page
        return render_template('success.html', amount=amount, receiver=receiver_account_number, sender=sender_account_number)
    else:
        # For simplicity, returning the response from the server if not successful (you can modify this as needed)
        return render_template('unsuccess.html', amount=amount, receiver=receiver_account_number, sender=sender_account_number)

if __name__ == '__main__':
    app.run(debug=True)
