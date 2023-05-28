import time
import board
import adafruit_tsl2591
from w1thermsensor import W1ThermSensor
import json

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the light sensor.
sensor = adafruit_tsl2591.TSL2591(i2c)

# Initialize the temperature sensor.
w1_sensor = W1ThermSensor()

# Create a list to store the data
data = []

# Start time at the current timestamp
start_time = time.strftime("%Y%m%d%H%M%S")

# Read the light levels and temperature every second.
while True:
    # Read and calculate the light levels.
    lux = sensor.lux
    infrared = sensor.infrared
    visible = sensor.visible
    full_spectrum = sensor.full_spectrum

    # Read and print the temperature.
    for w1_sensor in W1ThermSensor.get_available_sensors():
        temperature = w1_sensor.get_temperature()

    # Create a data dictionary for the current readings
    current_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "lux": lux,
        "infrared": infrared,
        "visible": visible,
        "full_spectrum": full_spectrum,
        "temperature": temperature
    }

    # Append the current data to the list
    data.append(current_data)

    # Write the data to a JSON file named after the start time
    file_name = "sensor_data_{}.json".format(start_time)
    with open(file_name, "w") as file:
        json.dump(data, file)

    time.sleep(1.0)
