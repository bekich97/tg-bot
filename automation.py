from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from pathlib import Path
from db import get_db_connection
import pathlib

# Get current file directory
this_dir = str(pathlib.Path(__file__).parent.resolve())

# Get user from database by nickname
def get_user(nickname):
    conn = get_db_connection()
    cursor = conn.cursor()
    qs = cursor.execute(f"SELECT * FROM users WHERE nickname='{nickname}'")
    fetched_data = qs.fetchall()
    if len(fetched_data):
        return fetched_data[0]
    else:
        return False

# First step of web form
def first_step(web, user):
    print("Running first step...")

    # Define firstname and lastname
    firstName = user[2]
    lastName = user[3]

    if not firstName:
        print("No first name")
        return False

    if not lastName:
        print("No last name")
        return False

    # Try to get web form elements
    first_name_input = None
    last_name_input = None

    try:
        first_name_input = web.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div[1]/div/div/div/input')
        last_name_input = web.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div[2]/div/div/div/input')
        next_button = web.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[3]/div/button')
    except:
        print("Some error on find first_name_input, last_name_input and next_button")
        return False

    # Pass values to input fields
    first_name_input.send_keys(firstName) 
    time.sleep(1)
    last_name_input.send_keys(lastName)
    time.sleep(1)
    next_button.click()

    return True

# Second step of web form
def second_step(web, user):
    print("Running second step...")

    email = user[4]
    phone = user[5]

    if not email:
        print("No email address")
        raise SystemExit

    if not phone:
        print("No phone number")
        raise SystemExit

    email_input = None
    phone_input = None

    try:
        email_input = web.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div[1]/div/div/div/input')
        phone_input = web.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div[2]/div/div/div/input')
        next_button = web.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/button')
    except:
        print("Some error on find email_input, phone_input and next_button")
        return False

    email_input.send_keys(email) 
    time.sleep(1)
    phone_input.send_keys(phone)
    time.sleep(1)
    next_button.click()

    return True

# Third step of web form
def third_step(web, user):
    print("Running third step...")

    date = user[6]

    if not date:
        print("No birth date")
        raise SystemExit

    date_input = None

    try:
        date_input = web.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div/div/div/div/div[1]/input')
        send_button = web.find_element(By.XPATH, '/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[4]/div[2]/button')
    except:
        print("Some error on find date_input and send_button")
        return False

    # date_input.clear()
    web.execute_script("document.getElementsByClassName('b24-form-control')[0].removeAttribute('readonly');")
    date_input.send_keys(date)
    time.sleep(1)
    send_button.click()

    return True

# Run automation
def run_automation(nickname):
    print("Running automation...")

    # Get user by nickname from database
    user = get_user(nickname)

    if not user:
        return False

    user_id = user[1]

    # Config for selenium chrome driver
    # chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # web = webdriver.Chrome('/home/medet/chromedriver', chrome_options=chrome_options)
    web = webdriver.Chrome()
    try:
        web.get("https://b24-iu5stq.bitrix24.site/backend_test")
    except:
        print("Connection error")
        raise SystemExit

    # Waiting for opening web page entirely
    time.sleep(5)

    fs = first_step(web, user)
    if not fs:
        return False
    time.sleep(1)
    ss = second_step(web, user)
    if not ss:
        return False
    time.sleep(1)
    ts = third_step(web, user)
    if not ts:
        return False
    
    # Wait until 
    time.sleep(10)

    # Get current datetime
    now_date = datetime.now()

    # Config of image full path with image name
    directory = f"{this_dir}/images/{now_date.year}/{now_date.month:02d}/{now_date.day:02d}/"
    img_name = f"{now_date.year}-{now_date.month:02d}-{now_date.day:02d}_{now_date.hour:02d}:{now_date.minute:02d}_{user_id}.jpg"

    # Create directory for images if not exists
    Path(directory).mkdir(parents=True, exist_ok=True)

    # Try to screenshot webpage and save image to the directory
    try:
        screenshot = web.get_screenshot_as_file(directory + img_name)
    except Exception as err:
        print("Some exception on taking screenshot", err)
        return False

    time.sleep(1)
    # Quit from browser and close
    web.quit()

    return True
