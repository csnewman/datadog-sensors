# datadog-sensors
DataDog plugin to report sensors metrics

## Instructions
* Install lm-sensors
```
sudo apt install lm-sensors 
```

* Detect sensors
```
sudo sensors-detect
```
(Save the file at the end)

* Install PySensors
```
/opt/datadog-agent/embedded/bin/pip install PySensors
```
* Copy over the custom check and check config file to the DataDog agent install directory   
```
cp sensors.yaml /etc/dd-agent/conf.d/
cp sensors.py /etc/dd-agent/checks.d/
```

* Restart the Datadog agent
