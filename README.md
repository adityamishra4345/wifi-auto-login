# 🚀 IIITG Wi-Fi Auto-Login

A lightweight Python automation script to bypass the repetitive captive portal login for the IIIT Guwahati campus network.

This script eliminates the need to manually enter credentials every time you connect. It uses Selenium to handle the web interface and authenticate automatically. It is built with secure coding practices, utilizing environment variables to ensure your personal credentials are never hardcoded or exposed to version control.

## ✨ Features
* Zero-Touch Login: Automatically fills in credentials and submits the captive portal form.
* Secure Credential Storage: Uses a hidden .env file to keep your password safely on your local machine.

## 🛠️ Technologies Used
* Python
* Selenium (for browser automation)
* python-dotenv (for secure credential management)
* os Module (for environment variable retrieval)

## ⚙️ Setup & Installation

1. Clone the repository:
git clone https://github.com/adityamishra4345/wifi-auto-login.git
cd wifi-auto-login

2. Install dependencies:
pip install selenium python-dotenv
(Note: You will also need the appropriate WebDriver for your browser, such as ChromeDriver, downloaded and extracted to desired location given in code).

4. Configure your credentials securely:
Create a new file named exactly .env in the root directory of the project. Add your login details like this (no quotes needed):
WIFI_USERNAME=your_actual_username
WIFI_PASSWORD=your_actual_password

5. Run the script:
python wifi_login.py

## 🤝 Forking & Contributing
Contributions are welcome! If you'd like to improve the script or adapt it for other campus networks, feel free to fork it:
1. Click the "Fork" button at the top right of this repository.
2. Clone your forked repository to your local machine.
3. Make your improvements and commit them.
4. Push to your fork and open a Pull Request!

## 🔒 Security Note
Never commit your .env file to version control. The included .gitignore file ensures your credentials stay hidden from GitHub.
