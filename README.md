# Email Automation

This is a Python application leveraging the SMTPLIB library for sending emails through a Gmail account.

## How to Use

1. Enable two-factor authentication on the sender's Gmail account [here](https://myaccount.google.com/signinoptions/two-step-verification).

2. Generate an "app password" for use in the email application. You cannot use your actual Gmail password. Generate it [here](https://myaccount.google.com/apppasswords).

3. Create a folder on your computer named "Transmission App". **Note**: Do not use the word "email" in the folder name, as it may cause issues with the SMTPLIB library.

4. Inside this folder, create a sub-folder named "templates".

5. Organize the files in this repository into the folder following this tree structure:

    ```plaintext
    Transmission App
    ├── app.py
    └── templates
        └── index.html
    ```

6. Open the folder in your chosen code editor. Save both files.

7. Install Flask in your terminal using the command:

    ```bash
    pip install Flask
    ```

8. Run the application in your terminal using the command:

    ```bash
    python app.py
    ```

9. Navigate to http://127.0.0.1:5000/ in your web browser. Enter the details into the form, and the email should be transmitted to your receiver's email address.
