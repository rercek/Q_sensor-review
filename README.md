# Q_sensor Review

## Introduction

This document gives a review about the precision of the following [ESP32-C6 multi sensor (alias Q_sensor)](https://www.tindie.com/products/adz1122/esp32-c6-multi-sensor-co2-voc-imu/) measurements:
- Temperatures given by the AHT20, BMP280 and SDC40 sensors
- Humidity given by the AHT20 and SDC40 sensors
- CO2 given by the SDC40 sensor

It also enlights some problems with the SDC40 and other sensors of the Q_sensor and also focused on adding several DS18B20 temperature probes to the Q_sensor. The code was directly based on the [zigbee one](https://github.com/xyzroe/Q_sensor).


## Material and methodology

### ESP32-C6 multi sensors

5 Q_sensors were ordered:
- 2 Q_sensors v2.1 on [Tindie](https://www.tindie.com/products/adz1122/esp32-c6-multi-sensor-co2-voc-imu/) with a SDC40 or SDC41 module (no laser marking on the sensor!, see [datasheet][https://sensirion.com/media/documents/48C4B7FB/64C134E7/Sensirion_SCD4x_Datasheet.pdf] page 24) directly soldered on the Q_senor PCB
- 3 Q_sensors v2.2 on [Aliexpress](https://fr.aliexpress.com/item/1005007922381128.html) with laser maked SDC40 module.

**Please note that both Q_sensors v2.1 had some ground connections issues with the PCB that were corrected and one Q_sensor v2.2 had power supply issues on the PCB (brownout detector triggered !)**

All Q_sensors wered modified to add a Onewire bus on GPIO 9 (BOOT) with a pull-up 4.7k resistor in order to connect up to 5 DS18B20, usually with 5m length (max 4x5m & 1x1m). A second onewire bus GPIO 1 on one of the Q_sensor v2.2 was also added in order to increase the number of DS18B20 to max 8 DS18B50 (usually 5-6) with 5m cables because there were too much reading errors with only one bus connecting 5 DS18B20 probes. 

Please note that the Q_sensor also contains a light sensor (BH1750 lux measurement), a radar for presence detection (BS5820), a VOC sensor (AGS10) and an IMU (QMI8658C) that have not been analyzed.  

### Other devices

In order to compare the measurements given by the Q_sensors, 3 other devices were used:
1. A [Xiaomi LYWSD03MMC with a custom zigbee firmware](https://www.zigbee2mqtt.io/devices/LYWSD03MMC-z.html#xiaomi-lywsd03mmc-z) measuring room temperature and humidy. 
2. A [TS0601 air quality sensor](https://www.zigbee2mqtt.io/devices/LYWSD03MMC-z.html#xiaomi-lywsd03mmc-z) measuring room temperature, humidity and CO2. This sensor alos gives VOC and Formaldehyd measurements which were not used.
3. A _DIY_ (Do-It-Yoursel) ESP32-C6, calle *R_sensor*, with a BME280 module for room temperature and humidity and a MH-Z19B for CO2. A HC SR501 PIR detector (for presence detection) and a BH1750 light sensor were also connected to this device but were not used. 


### Experimental measurement campaign

In total, 6 Zigbee devices were used in a 14-day measurement campaign, including 3 Q_sensors without their case and the 3 devices described in the previous section. The devices with their name/Zigbee address is given below:
1. `0x404ccafffe571d50`: Q_sensor v2.1 without DS18B20 probe
2. `0x404ccafffe56dcbc`: Q_sensor v2.2 with 1 DS18B20 probe
3. `0x404ccafffe56dd00`: Q_sensor v2.2 with 2 onewire buses each connecting 4 DS18B20 probes (total 8 probes)
4. `0xa4c138c8b4cad0f7`: Xiaomi LYWSD03MMC 
5. `0xa4c138901f2c788c`: TS0601 air quality sensor
6. `0x588c81fffe37b37c`: R_sensor 

As the following image shows, all devices were placed on a desk in a office room where a person might occasionally be present next to the devices.

[!Experimant pictures](./images/Experiment.jpg)


All devices were connected to a USB Zigbee coordinator dongle in the same room using [Zigbee2MQTT](https://www.zigbee2mqtt.io/) with a reporting of maximum 10min for each Q_sensor and R_sensor measurement on a installed mqtt server [`mosquitto`](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html), 1h for the LYWSD03MMC device and unknown for the TS0601 air quality sensor (but probably a few second as specified in the Notes of this [link](https://www.zigbee2mqtt.io/devices/TS0601_air_quality_sensor.html#tuya-ts0601_air_quality_sensor)).

In order to easily record measurements sent by different devices in a time series [influx2 database](https://docs.influxdata.com/influxdb/v2/), [Home-Assistant](http://home-assistant.io/) was configured to use the same mqtt server as Zigbee2MQTT and correctly configure [Zigbee2MQTT for Home-Assistant](https://www.zigbee2mqtt.io/guide/usage/integrations/home_assistant.html). In parallel, Home-Assistant was linked to [an external influx2 database](https://www.home-assistant.io/integrations/influxdb/).

Finaly, to easily analyse the precision of the measurements in the influx2 database, a [grafana](https://grafana.com) dashboard using the influx2 database as source was created. 


## Results and discussion

### Temperature

### Humidity 

### CO2

### Remarks




## Conlusion


