import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Loads the hidden file
load_dotenv()

# Safely fetch your credentials using LABELS
USERNAME = os.getenv('WIFI_USER')
PASSWORD = os.getenv('WIFI_PASS')

# --- CONFIGURATION ---
LOGIN_URL = "https://secure.iiitg.ac.in:8090"  
DRIVER_PATH = r"C:\Users\ADTIYA MISHRA\OneDrive\Desktop\Wifi\chromedriver.exe"               
# ---------------------

print("Starting Wi-Fi Login with Local Driver...")

opt = Options()


# Removing the '#' makes Chrome run completely invisibly in the background!
opt.add_argument("--headless=new") 

# Anti-error flags
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('--ignore-ssl-errors')
opt.add_argument('--allow-insecure-localhost')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# Keeps the hidden browser process alive so the firewall doesn't log you out
opt.add_experimental_option("detach", True)

# I am commenting out Headless mode for now. 
# Sophos/Cyberoam firewalls often disconnect if the browser window doesn't stay alive in the background.
# opt.add_argument("--headless=new") 

# Anti-error flags
opt.add_argument('--ignore-certificate-errors')
opt.add_argument('--ignore-ssl-errors')
opt.add_argument('--allow-insecure-localhost')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

# Keeps browser open so the firewall doesn't log you out
opt.add_experimental_option("detach", True)

try:
    print(f"1. Loading local ChromeDriver...")
    driver_service = Service(DRIVER_PATH)
    
    print("2. Opening Chrome...")
    driver = webdriver.Chrome(service=driver_service, options=opt)
    
    print(f"3. Connecting to the campus portal...")
    driver.get(LOGIN_URL)
    
    print("4. Waiting for the login box to appear...")
    wait = WebDriverWait(driver, 10)
    user_box = wait.until(EC.presence_of_element_located((By.ID, "username")))
    
    print("5. Typing credentials...")
    user_box.clear()
    # Notice: NO quotes around USERNAME!
    user_box.send_keys(USERNAME)

    pass_box = driver.find_element(By.ID, "password")
    pass_box.clear()
    # Notice: NO quotes around PASSWORD!
    pass_box.send_keys(PASSWORD)

    print("6. Pressing Enter...")
    pass_box.send_keys(Keys.RETURN) 
    
    print("7. Waiting for the network handshake...")
    time.sleep(5) # Gives the firewall time to register your machine
    
    print("Done! You should be connected to the internet.")

except Exception as e:
    print(f"\n--- SCRIPT CRASHED ---")
    print(f"Error Details: {e}")