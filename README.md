# Product Sniper

The Product Sniper is a neat application that allows you to check if an item on a webpage is available!

This project is a work in progress, so please feel free to request any features or bug fixes.

## Documentation

### Prerequisites

In order to use this application, you will need to install two Python libraries:

1. [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - for pulling data out of HTML websites. 
2. [Requests](https://requests.readthedocs.io/en/master/) - allows you to send HTTP requests easily.

To install them, do a simple `pip3 install bs4 requests` in your terminal.

Alternatively, you can do a `pip3 install -r requirements.txt`. This will install everything directly from that .txt file.

Thats it!

(If you come across any issues, please refer to their documentation or request an issue in the repo).

### Installation
Clone the repository using git onto your computer.

![image](https://user-images.githubusercontent.com/76453314/111336206-eca8af80-866c-11eb-831b-04a9631ec62b.png)

OPTIONAL: Create a new file in that same directory and name it 'login.py'. This is where you will store your for_email, to_email and password.

If you aren't going to be sharing your script, then simply replace the two from_email with an email you want to receive from, replace the to_email with an email you want to send to (you can use the same email as the from one).

There are two ways for using the password, one way is without 2FA and one is with 2FA. In this I'm going to be using 2FA with Gmail.

For the password, you would need to know if you 2FA enabled on your email account.

If you're not sure how, Google 'how to enable EMAIL PROVIDER 2 factor authentication'

For Gmail users:

1. Open your Google account.
2. In the left side panel, select Security.
3. Under “Signing in to Google,” select 2-Step Verification and then Get started.
4. Follow the on-screen steps.

After you know its enabled, create an app password which will grant access to the application to send an email without having to provide too much information.

For Gmail users:

1. Open your Google account.
2. In the left side panel, select Security.
3. Under “Signing in to Google,” select App Passwords.
4. Click on "Select app" and choose 'Mail'.
5. Select your device (usually Mac or Windows Computer).
6. Copy the password it provides and make sure not to lose it, you can't click on it to retrieve. If you somehow lose it, just delete the app password and create another one.

Now you're pretty much done! Just put the password into where it says password, and get rid of the `from login import from_email, to_email, password` if you put your details right into the script instead of a separate file.
