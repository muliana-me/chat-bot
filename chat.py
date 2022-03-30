import pyautogui
import time

def send():
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

print('\nCHAT BOT')
print('````````')
print('\nCopy the message that you want to send.')
input('Press [Enter] to continue')

chat = input('\nTotal chat: ')
delay = input('Time delay (second): ')
input('Press [Enter] to start')

print('\nOpen your App. Dont close the App until its done.')
print('Bot is running.')

time.sleep(6)
for x in range(int(chat)):
    send()
    time.sleep(int(delay))

print('\n\nDone.\n`````\n')