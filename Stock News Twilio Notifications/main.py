import requests
import smtplib
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = '**********************'
NEWS_API_KEY = '**********************'
MYEMAIL = 'invictusdev25@gmail.com'
PASSWORD = MY_OWN_PASSWORD # Environment variable
account_sid = '**********************'
auth_token = '**********************'

stockParams = {                            # These parameters are required to be filled according to the structure of
    "function": "TIME_SERIES_DAILY",     # https://www.alphavantage.co/query APIs
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stockParams)
# print(response.json())
data = response.json()["Time Series (Daily)"]
print(data)
dataOfDays = [value for (key, value) in data.items()] # It is necessary to receive a list with all days to be able to extract each day seperately
print(dataOfDays)
previousDay = dataOfDays[0]
previousClosePrice = previousDay["4. close"]
print(previousClosePrice)

# Getting the day before yesterday's closing stock price
dayBeforePreviousDay = dataOfDays[1]
day_before_previousDayClosePrice = dayBeforePreviousDay["4. close"]
print(day_before_previousDayClosePrice)

# Finding the positive difference between 1 and 2.
difference = float(previousClosePrice) - float(day_before_previousDayClosePrice)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

print(difference)

# Calculating percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentageRatio = round((difference / float(previousClosePrice)) * 100)
print(percentageRatio)

# Using the News API to get articles related to the COMPANY_NAME.
if abs(percentageRatio) > 1:
    newsParams = {
        "q": COMPANY_NAME,      # Keywords or phrases to search for in the article title and body.
        "apiKey": NEWS_API_KEY,
    }
    newsResponse = requests.get(NEWS_ENDPOINT, params=newsParams) # Using requests to get hold some of data from this endpoint
    allArticles = newsResponse.json()['articles']
    print(allArticles)


    # Using Python slice operator to create a list that contains the first 3 articles.
    firstThreeArticles = allArticles[:3]
    print(firstThreeArticles)


    ## STEP 3: Use twilio to send a separate message with each article's title and description to a phone number.

# Creating a new list of the first 3 article's headline and description using list comprehension.
    listOfDescriptions = [f"{STOCK_NAME}: {up_down}{percentageRatio}%\nHeadline: {article['title']}.Brief: {article['description']}" for article in firstThreeArticles]
    print(listOfDescriptions)

    client = Client(account_sid, auth_token)

    for article in listOfDescriptions:
        formattedArticle = ''.join(article).encode('utf-8').strip()
        print(formattedArticle)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MYEMAIL, password=PASSWORD)

            connection.sendmail(
                from_addr=MYEMAIL,
                to_addrs=MYEMAIL,
                msg=f"LAST NEWS\n\n{formattedArticle}"
            )

        #client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=article,
                from_='+18445932434',
                to='+1646*******'
            )
print(message.sid)
