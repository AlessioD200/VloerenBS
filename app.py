from flask import Flask, render_template, request, flash, redirect, url_for
import os
import smtplib

# Initialize Flask app
app = Flask(__name__)

# Secret key for session management, loaded from environment variables
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "fallback_dev_key")

# Homepage route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        # Validate form data
        if not name or not email or not message:
            flash('Alle velden (behalve telefoonnummer) zijn verplicht!', 'error')
            return redirect(url_for('index'))

        try:
            # Send the email
            send_email(name, email, phone, message)
            flash('Bedankt voor uw aanvraag! We nemen spoedig contact met u op.', 'success')
        except Exception as e:
            flash('Er is een fout opgetreden bij het verzenden van de e-mail.', 'error')
            print(f"Error: {e}")

        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/projecten')
def projecten():
    return render_template('projecten.html')

@app.route('/beoordelingen')
def beoordelingen():
    return render_template('beoordelingen.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


def send_email(name, email, phone, message):
    # Load email credentials from environment variables
    sender_email = os.environ.get('SENDER_EMAIL')  # Use environment variable for sender email
    sender_password = os.environ.get('SENDER_PASSWORD')  # Use environment variable for sender password
    receiver_email = os.environ.get('RECEIVER_EMAIL')  # Use environment variable for receiver email
    if not all([sender_email, sender_password, receiver_email]):
        raise Exception("Environment variables for email not configured properly.")
    
    subject = "Nieuwe aanvraag via Vloeren BS"
    body = f"""
    Naam: {name}
    E-mail: {email}
    Telefoon: {phone or 'Geen telefoonnummer opgegeven'}
    Bericht:
    {message}
    """

    # Sending the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{body}")
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")


# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
