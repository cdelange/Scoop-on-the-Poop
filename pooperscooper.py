from gpiozero import Button, LED
import requests
from signal import pause
from time import sleep

# Each dog (Nova and Zuri) has their own button for poos and pees

zuri_poop = Button(4, pull_up=False)
zuri_pee = Button(18, pull_up=False)
nova_poop = Button(23, pull_up=False)
nova_pee = Button(24, pull_up=False)
delete_button = Button(25, pull_up=False)  # initalizes a button to delete most recent database post
id_switch = Button(8, pull_up=False)  # id swithc for casey or allie

success_led = LED(22)
failure_led = LED(27)


def post(channel):
        success_led.on()  # green led lights up while POST request is created and processed
        person = id_switch.value
        buttonNamesDict = {4: {'dog': 'Zuri', 'typeOfBreak': 'Poop'}, 18: {'dog': 'Zuri', 'typeOfBreak': 'Pee'}, 23: {'dog': 'Nova', 'typeOfBreak': 'Poop'}, 24: {'dog': 'Nova', 'typeOfBreak': 'Pee'}}
        # this dictionary links the raspberry pi' BCM GPIO values to the keywords the Django form can properly process.

        payload = {'Dog': buttonNamesDict[channel.pin.number]['dog'], 'typeOfBreak': buttonNamesDict[channel.pin.number]['typeOfBreak'], 'walker': person}  # prepares the payload to be sent with the POST request

        try:
                r = requests.post('https://thescooponthepoops.herokuapp.com/buttons/', data=payload)

                if r.status_code == 200:  # if POST request succeeds
                        success_led.off()
                        sleep(.15)
                        success_led.blink(on_time=.15, off_time=.15, n=2)
                        print("Successful post! Server returned a status code of 200")

                else:   # if POST request fails
                        success_led.off()
                        sleep(.15)
                        failure_led.blink(on_time=.15, off_time=.15, n=2)
                        print("Failed to post because of status code")
        except:
                success_led.off()
                sleep(.15)
                failure_led.blink(on_time=.15, off_time=.15, n=2)
                print("Failed to post because of script error")


def delete(channel):  # django form for /delete is set up to delete the most recent database entry if it recieves a post request of any kind.

        success_led.on()
        failure_led.on()

        try:
                r = requests.post('https://thescooponthepoops.herokuapp.com/delete/')

                if r.status_code == 200:
                        success_led.off()
                        failure_led.off()
                        sleep(.15)
                        success_led.blink(on_time=.15, off_time=.15, n=2)
                        print("Successful delete! Server returned a status code of 200")
