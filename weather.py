import adafruit_bme680
import time
import board

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

temperature_offset = -5

while True:
  temperature_f = (bme680.temperature * 9/5) + 32
  altitude_ft = bme680.altitude * 3.28084
  pressure_inhg = bme680.pressure * 0.02953

  print("\nTemperature: %0.1f F" % (temperature_f + temperature_offset))
  print("Humidity: %0.1f %%" % bme680.relative_humidity)
  print("Pressure: %0.3f inHg" % pressure_inhg)
  print("Altitude = %0.2f feet" % altitude_ft)
  
  time.sleep(3)
