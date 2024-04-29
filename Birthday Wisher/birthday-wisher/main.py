import datetime as dt
import pandas
import random
import smtplib
import re
MYEMAIL = 'invictusdev25@gmail.com'
PASSWORD = "*****************"

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
# print(data)

# for (index, dataRow) in data.iterrows():
#     print(dataRow)
#     print(index)
#     print(dataRow["month"])

birthdaysDict = {(dataRow["month"], dataRow["day"]): dataRow for (index, dataRow) in data.iterrows()}  # iterrows() method allows to iterate through dataframe
                                # and then we can get hold of the index of each of those rows and also the data in each of the rows.
#print(birthdaysDict)

if today in birthdaysDict:
    birthdayPerson = birthdaysDict[today] # We have access the data row for that particular match
    print(birthdayPerson)
    print(birthdayPerson['name'])
    filePath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filePath) as letterFile:
        content = letterFile.read()
        #content.replace('[NAME]', birthdayPerson['name'])  # Extracting name of a person.
        contentNew = re.sub('NAME', birthdayPerson['name'], content)
        #print(content)
        print(contentNew)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MYEMAIL, password=PASSWORD)

        connection.sendmail(
            from_addr=MYEMAIL,
            to_addrs=birthdayPerson['email'],
            msg=f"Subject: Birthday Wish\n\n{content}" # content is a randomly selected letter with a wish
        )



