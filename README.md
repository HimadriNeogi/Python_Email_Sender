# Python Email Sender

This project provides a simple yet effective Python script to send emails with attachments (PDF, DOCX, XLSX) to multiple recipients using Gmail's SMTP server.

---

## Features

* **Customizable Sender:** Easily configure your Gmail address and app password.
* **Multiple Recipients:** Send emails to a list of specified email addresses.
* **Dynamic Subject & Body:** Set the subject and content of your email.
* **Attachment Support:** Attach PDF, DOCX, and XLSX files. 
* **Error Handling:** Basic error handling to inform you if an email fails to send to a particular recipient.

---

## Prerequisites

Before you run this script, ensure you have the following:

* **Python 3.x:** Installed on your system.
* **Gmail Account:** The sender email address must be a Gmail account.
* **Gmail App Password:** You **must** generate an app password for your Gmail account to use with this script. Regular Gmail passwords will not work due to security restrictions.
    * **How to Generate an App Password:**
        1.  Go to your Google Account.
        2.  Navigate to **Security**.
        3.  Under "How you sign in to Google," select **2-Step Verification**. (If it's off, you'll need to enable it first).
        4.  Scroll down to **App passwords** and click it.
        5.  Follow the instructions to generate a new app password. You'll get a 16-character code; this is your `sender_pw`.

---

## Setup and Usage

1.  **Clone the repository** or download the `email_sender.py` file.
    ```bash
    git clone [https://github.com/HimadriNeogi/Python_Email_Sender.git](https://github.com/HimadriNeogi/Python_Email_Sender.git)
    cd Python_Email_Sender
    ```

2.  **Update the configuration variables:**
    * `email_ids`: Add the recipient email addresses to this list.
    * `sender_id`: Replace `"your_email@gmail.com"` with your actual Gmail address.
    * `sender_pw`: Replace `"your_app_password"` with the 16-character app password you generated.
    * `subject`: Customize your email subject.
    * `body`: Write the content of your email.


3.  **Place your attachment file** in the same directory as the `email_sender.py` script.

4.  **Run the script** from your terminal. You will see output indicating whether the emails were sent successfully or if any failures occurred.

---

## Contributing

Feel free to fork this repository, open issues, or submit pull requests if you have suggestions for improvements or bug fixes!
