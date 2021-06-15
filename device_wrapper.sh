#!/bin/bash

# 5.12.2018
# Wrapper zum Starten von BronkhorstPressureCtrl.py 

# Exportieren der Variable TANGO_HOST fuer die Bash-Shell

export TANGO_HOST=newton.nano.lab:10000

TANGOHOST=newton.nano.lab

#Umleiten der Ausgabe in eine Log-Datei
exec &>> /home/pi/TangoDS/pytango-BronkhorstPressureCtrl/device.log

echo "---------------------------"
echo $(date)
echo "Tangohost: " $TANGOHOST

# Warten bis der Tangohost sich meldet
while ! timeout 0.2 ping -c 1 -n $TANGOHOST &> /dev/null
do
  :
# mache nix  
done

echo "ping Tangohost successful!"
echo "starting BronkhorstPressureCtrl device"

# Fork/exec
(
  exec /usr/bin/python3 /home/pi/TangoDS/pytango-BronkhorstPressureCtrl/BronkhorstPressureCtrl.py raspi03 -v2&
) 
&>> /home/pi/TangoDS/pytango-BronkhorstPressureCtrl/device.log 
