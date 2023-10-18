
import datetime as dt
import pandas
import random
import smtplib

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

df = pandas.DataFrame(data)
data_dict = df.to_dict()

now = dt.datetime.now()
day = now.day
month = now.month

# 2. Check if today matches a birthday in the birthdays.csv
for i in range(0, len(data_dict["name"])):
    if month == data_dict["month"][i] and day == data_dict["day"][i]:
        b_name = data_dict["name"][i]
        mail = data_dict["email"][i]

        letter_picked = f"letter_templates/letter_{random.randint(1 ,3)}.txt"
        with open(letter_picked) as file:
            letter = file.read()

            letter = letter.replace("Dear [NAME]", b_name)

            my_email = "your mail" # replace with your email
            password = "your password" # replace with your password generated for an app

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=mail,
                    msg=f"Subject:Birthday Message\n\n {letter}"
                )
