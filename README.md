# Scoop-on-the-Poop
A project that links a real-world interface to a SQL database using to Django, Python, and a Raspberry Pi to track and display the bathrooms breaks of my dogs on a webpage. This allows all members of my household to check if it is time for dogs to go out and eliminates the need for repetitive texting between household members.

The Python script runs on the Raspberry Pi and listens for inputs from specific GPIO pins on the Pi that are connected to analog arcade buttons. There are 4 buttons total for each dogs poops and pees. There is also a button for deleting the most recent input and a SPDT switch to choose which housemember is inputing the bathroom break.

When a button is pressed (Zuri Pee for example), a Post request is sent to https://thescooponthepoops.herokuapp.com/ and stored in the database.

## Built With
* Python
* Django
* ssh

## Acknowledgments

* Zuri and Nova

