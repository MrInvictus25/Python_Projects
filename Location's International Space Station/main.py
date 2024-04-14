import requests
import datetime as dt
import smtplib
import time

MY_LAT = 40.712776   # New York
MY_LNG = -74.005974  # New York
MYEMAIL = 'invictusdev25@gmail.com'
PASSWORD = MY_OWN_PASSWORD # Environment variable

def is_iss_overhead(): # whether if the ISS is at a similar position to my position,
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

def is_night():  # whether if it's nighttime or not.
    parameters = {
        "lat": MY_LAT,  # These values in sunrise-sunset apis are mandatory
        "lng": MY_LNG,
        "formatted":0  # Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # Extracting an hour
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])   # Extracting an hour

    print(sunrise)
    print(sunset)

    timeNow = dt.datetime.now().hour
    # print(timeNow.hour)

    if timeNow >= sunset or timeNow <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MYEMAIL, password=PASSWORD)

            connection.sendmail(
                from_addr=MYEMAIL,
                to_addrs=MYEMAIL,
                msg="LOOK UP ON ISS\n\nThe ISS is above your head in the Sky!"
            )
