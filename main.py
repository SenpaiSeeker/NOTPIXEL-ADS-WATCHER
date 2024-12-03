import subprocess
import time
import signal
import os
import base64
from termcolor import colored
import itertools

# Encode your banner in base64 and replace the placeholder
encoded_banner = "CgorLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKwp8IOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilZcg4paI4paI4paI4paI4paI4paI4paI4paI4pWX4paI4paI4pWXICAgIOKWiOKWiOKWiOKVlyAgIOKWiOKWiOKWiOKVlyDilojilojilojilojilojilZcg4paI4paI4pWXICAgICB8CnzilojilojilZTilZDilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZfilZrilZDilZDilojilojilZTilZDilZDilZ3ilojilojilZEgICAg4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVkSAgICAgfAp84paI4paI4pWRICAg4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pWU4pWdICAg4paI4paI4pWRICAg4paI4paI4pWRICAgIOKWiOKWiOKVlOKWiOKWiOKWiOKWiOKVlOKWiOKWiOKVkeKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVkeKWiOKWiOKVkSAgICAgfAp84paI4paI4pWRICAg4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWdICAgIOKWiOKWiOKVkSAgIOKWiOKWiOKVkSAgICDilojilojilZHilZrilojilojilZTilZ3ilojilojilZHilojilojilZTilZDilZDilojilojilZHilojilojilZEgICAgIHwKfOKVmuKWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkSAgICAgICAg4paI4paI4pWRICAg4paI4paI4pWRICAgIOKWiOKWiOKVkSDilZrilZDilZ0g4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilojilojilojilojilojilZd8Cnwg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIOKVmuKVkOKVnSAgICAgICAg4pWa4pWQ4pWdICAg4pWa4pWQ4pWdICAgIOKVmuKVkOKVnSAgICAg4pWa4pWQ4pWd4pWa4pWQ4pWdICDilZrilZDilZ3ilZrilZDilZDilZDilZDilZDilZDilZ18CnwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8Cnwg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKVlyAgICDilojilojilZcgICAg4paI4paI4pWXICAg4paI4paI4pWX4paI4paI4paI4paI4paI4paI4paI4paI4pWXICB8CnzilojilojilZTilZDilZDilZDilZDilZ0g4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWU4pWQ4pWQ4pWQ4paI4paI4pWX4paI4paI4pWRICAgIOKWiOKWiOKVkSAgICDilZrilojilojilZcg4paI4paI4pWU4pWd4pWa4pWQ4pWQ4paI4paI4pWU4pWQ4pWQ4pWdICB8CnzilojilojilZEgIOKWiOKWiOKWiOKVl+KWiOKWiOKWiOKWiOKWiOKWiOKVlOKVneKWiOKWiOKVkSAgIOKWiOKWiOKVkeKWiOKWiOKVkSDilojilZcg4paI4paI4pWRICAgICDilZrilojilojilojilojilZTilZ0gICAg4paI4paI4pWRICAgICB8CnzilojilojilZEgICDilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZEgICDilojilojilZHilojilojilZHilojilojilojilZfilojilojilZEgICAgICDilZrilojilojilZTilZ0gICAgIOKWiOKWiOKVkSAgICAgfAp84pWa4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWRICDilojilojilZHilZrilojilojilojilojilojilojilZTilZ3ilZrilojilojilojilZTilojilojilojilZTilZ0gICAgICAg4paI4paI4pWRICAgICAg4paI4paI4pWRICAgICB8Cnwg4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdIOKVmuKVkOKVnSAg4pWa4pWQ4pWdIOKVmuKVkOKVkOKVkOKVkOKVkOKVnSAg4pWa4pWQ4pWQ4pWd4pWa4pWQ4pWQ4pWdICAgICAgICDilZrilZDilZ0gICAgICDilZrilZDilZ0gICAgIHwKKy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSsKCg=="  # OPTIMALGROWYT

def decode_banner(encoded_banner):
    """Decode the base64 encoded banner."""
    try:
        decoded_banner = base64.b64decode(encoded_banner).decode('utf-8')
        return decoded_banner
    except Exception as e:
        print(f"Error decoding banner: {e}")
        return None

def display_gradient_banner():
    """Display a gradient colored banner in the terminal."""
    banner = decode_banner(encoded_banner)
    if banner:
        gradient_colors = itertools.cycle(['red', 'yellow', 'green', 'blue', 'magenta', 'cyan'])
        print("Decoded and displaying banner with gradient colors:")
        for char, color in zip(banner, gradient_colors):
            print(colored(char, color), end="")
        print()  # For a newline after the banner

def display_additional_info():
    """Display the additional information with colored text."""
    print(colored('CREATED BY : DR ABDUL MATIN KARIMI: ⨭ ', 'yellow') + colored('https://t.me/doctor_amk', 'green'))
    print(colored('JOIN OUR TELEGRAM CHANNEL ➤ ', 'white') + colored('https://t.me/optimalgrowYT', 'green'))
    print(colored('LEARN HACKING HERE ➤ ', 'red') + colored('https://www.youtube.com/@optimalgrowYT/videos', 'green'))
    print(colored('DOWNLOAD MORE HACKS ➤ ', 'red') + colored('https://github.com/OptimalGrowYT', 'green'))
    print(colored('BUY NODEPAY REFERAL HERE ➤ : ⨭ ', 'white') + colored('https://t.me/doctor_amk', 'green'))
    print(colored('PASTE YOUR [QUERY] INTO QUERY_ID.TXT FILE AND PRESS START ', 'yellow'))
    print(colored('                  [𝍖𝍖𝍖 NOTPIXEL ADS WATCHER 𝍖𝍖𝍖]                  ', 'green'))

def run_script_continuously():
    while True:
        # Display the gradient banner
        display_gradient_banner()
        
        # Display additional info
        display_additional_info()
        
        # Start the script and leave it running indefinitely
        process = subprocess.Popen(['python3', 'script.py'])
        print("Started script.py with PID:", process.pid)
        
        # Wait indefinitely (no time.sleep or termination)
        process.wait()  # This will make the program wait for the script to finish, if ever

if __name__ == "__main__":
    run_script_continuously()
