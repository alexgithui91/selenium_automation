import smtplib

smtpObj = smtplib.SMTP("smtp-mail.outlook.com", 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("alexgithui91@outlook.com", "al3xg1thu1")
smtpObj.sendmail(
    "alexgithui91@outlook.com",
    "alexgithui91@gmail.com",
    "Subject: So long.\nDear Alex, so long and thanks for all the fish. Sincerely, Testing",
)
smtpObj.quit()
