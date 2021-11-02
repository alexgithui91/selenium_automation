import os
from dotenv import load_dotenv

# Get Freshdesk username and password
load_dotenv()
username = os.environ.get("secretUser")
password = os.environ.get("secretPassword")


def main():
    """Connect to Freshdesk and export tickets data"""
    pass


if __name__ == "__main__":
    main()
