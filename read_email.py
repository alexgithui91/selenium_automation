import imapclient

imapObj = imapclient.IMAPClient("imap-mail.outlook.com", ssl=True)

imapObj.login("agithui@dayliff.com", "al3xg1thu1")

imapObj.select_folder("INBOX", readonly=True)

# UIDs = imapObj.search(["UNSEEN"])

# print(UIDs)
