import subprocess

# Install required libraries
libraries = [
    'w1thermsensor',
    'adafruit_tsl2591',
    'adafruit-python-shell'
]

for library in libraries:
    subprocess.run(['sudo', 'pip3', 'install', library])

# Enable I2C interface
subprocess.run(['sudo', 'raspi-config', 'nonint', 'do_i2c', '0'])

# Enable One Wire interface
subprocess.run(['sudo', 'raspi-config', 'nonint', 'do_onewire', '0'])

# Download and run raspi-blinka.py script
subprocess.run(['wget', 'https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py'])
subprocess.run(['sudo', 'python3', 'raspi-blinka.py'])
