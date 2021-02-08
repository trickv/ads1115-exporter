#!/usr/bin/env python

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from prometheus_client import Info, Gauge
from prometheus_client import start_http_server

i = Info("ads1115_exporter", "Prometheus exporter to read votages on sensors attached to an ads1115 chip, on a Raspberry Pi.")
i.info({'version': '0'})

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
a0 = AnalogIn(ads, ADS.P0)
a1 = AnalogIn(ads, ADS.P1)
a2 = AnalogIn(ads, ADS.P2)
a3 = AnalogIn(ads, ADS.P3)

# Create Prom gauges
a0_gauge = Gauge("ads1115_a0", "fixme")
a1_gauge = Gauge("ads1115_a1", "fixme")
a2_gauge = Gauge("ads1115_a2", "fixme")
a3_gauge = Gauge("ads1115_a3", "fixme")

start_http_server(9898)
while True:
    a0_gauge.set(a0.voltage)
    a1_gauge.set(a1.voltage)
    a2_gauge.set(a2.voltage)
    a3_gauge.set(a3.voltage)

    print("sleeping 1");
    time.sleep(1)
