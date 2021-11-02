import smtplib

smtpObj = smtplib.SMTP("smtp-mail.outlook.com", 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("alex.githui@dayliff.com", "al3xg1thu1")
# smtpObj.sendmail(
#     "agithui@dayliff.com",
#     "agithui@dayliff.com",
#     "Subject: So long.\nDear Alex, so long and thanks for all the fish. Sincerely, Testing",
# )
# smtpObj.quit()
