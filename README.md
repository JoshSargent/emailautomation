# Email Automation
An application that uses the SMTPLIB library in Python to send emails from a Gmail account.


How to Use:

. Enable two-factor-authentication on the sender Gmail account at this link: https://myaccount.google.com/signinoptions/two-step-verification

. Generate an "app password" for use in the email application, as you cannot use your actual Gmail password. You can so at this link: https://myaccount.google.com/apppasswords

. Create a folder on your computer named "Transmission App". DO NOT use the word "email" in the folder name as this can cause issues with the SMTPLIB library. 

. Inside this folder, create a sub-folder named "templates".

. Place the files in this repository into the folder in this tree structure:

Transmission App
├── app.py
└── templates
    └── index.html

. Open the folder in your chosen code editor. Save both files.
. Install Flask in your terminal using the command, "pip install Flask".
. Run the application in your terminal using the command, "python app.py".

. Navigate to http://127.0.0.1:5000/ in your web browser. Enter the details into the form, and the email should be transmitted to your reciever email address.



