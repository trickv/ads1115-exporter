# ads1115-exporter
Prometheus exporter to read votages on sensors attached to an ads1115 chip, on a Raspberry Pi.

Based on code from my [Ambient Weather Exporter](https://github.com/trickv/ambient-weather-exporter)

# Libraries

* [prometheus/client_python](https://github.com/prometheus/client_python) - lets me register a series of metrics and runs a simple web server exposing the data read from Ambient as Prometheus metrics.
* TODO

# What it looks like

[You came for a graph, so here's one](http://ip.v9n.us/?fixme)

# How to use

- Get a pi and an ads1115
- wire it up
- git clone and run this thing with no parameters
- curl http://localhost:8000/
- Then configure Prom to scrape it every 60 seconds.
