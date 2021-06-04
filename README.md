# Product Sniper

The Product Sniper is a neat application that allows you to check if an item on a webpage is available!

Pretty much just tracks a webpage element with a way to indicate the products availability.

Demonstration can be shown [here](https://youtu.be/mdhT49qm3yI).

The documentation is mostly aimed at developers, but feel free to follow along!

## Setup

1. Click [here](https://github.com/pzrsa/product-sniper/fork) to fork this repo.
2. Clone your forked repo
```
# Replace `YOUR_GITHUB_USERNAME` with your own github username
git clone https://github.com/YOUR_GITHUB_USERNAME/product-sniper.git product-sniper
cd product-sniper

# Create a virtual environment and activate it
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
3. To get updates via email you need to setup an app password for Gmail, this can be done through [here](https://support.google.com/accounts/answer/185833/sign-in-with-app-passwords).
4. Replace the `from_email` and `from_email_password` with the details for the email that will be used to send updates. For the `to_email` you can put in the same one used when sending messages.
5. The current link its tracking is a PS5 on Amazon UK, however you can change it and track a different item. Keep in mind you do need to change what page element it should track through its id or class. If you know how CSS works then this should be easy for you to complete.
6. Run the application and if any errors pop up, feel free to open an issue and I'll be happy to help.

I hope it helps you just track pretty much anything on a page!
