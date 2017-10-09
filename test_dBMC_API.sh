#!/bin/sh
echo "Test script has started"

echo "dBMC_API is starting"
gnome-terminal -e "python ./dBMC-API/app.py"
sleep 5
echo "dBMC_API has started"

echo "SDMAgent is starting"
gnome-terminal -e "python ./SDMAgent/app.py"
sleep 5
echo "SDMAgent has started"


echo "Testing Switches"



echo "SwitchInfo Test"
curl -H "Content-Type: application/json" -X GET -d '{"dRackId":"0","dBoxId":"1","switchId":"11"}' http://localhost:5001/api/switch/info

echo "SwitchConnectPorts Test"
curl -H "Content-Type: application/json" -X POST -d '{"dRackId":"0","dBoxId":"1","switchId":"11", "ports": "[[11,22],[12,25]]"}' http://localhost:5001/api/switch/connectports

echo "SwitchDisconnectPort Test"
curl -H "Content-Type: application/json" -X POST -d '{"dRackId":"0","dBoxId":"1","switchId":"11", "ports": "[[11,22],[11,22]]"}' http://localhost:5001/api/switch/disconnectports

echo "SwitchPortEndPoint Test"
curl -H "Content-Type: application/json" -X POST -d '{"dRackId":"0","dBoxId":"1","switchId":"11", "portId": "11"}' http://localhost:5001/api/switch/portendpoint

echo "SwitchPortsInfo Test"
curl -H "Content-Type: application/json" -X GET -d '{"dRackId":"0","dBoxId":"1","switchId":"11"}' http://localhost:5001/api/switch/portsinfo

echo "SwitchPowerUtilization Test"
curl -H "Content-Type: application/json" -X GET -d '{"dRackId":"0","dBoxId":"1","switchId":"11"}' http://localhost:5001/api/switch/powerutilization


echo "Switch Test Completed Successfuly"


echo "Testing DBox"

echo "DBox Test"
curl -H "Content-Type: application/json" -X GET -d '{"dRackId":"0","dBoxId":"1"}' http://localhost:5001/api/dbox/info

echo "DboxTemperature Test"
curl -H "Content-Type: application/json" -X GET -d '{"dRackId":"0","dBoxId":"1"}' http://localhost:5001/api/dbox/temperature

echo "DboxPower Test"
curl -H "Content-Type: application/json" -X GET -d '{"dRackId":"0","dBoxId":"1"}' http://localhost:5001/api/dbox/power

echo "DboxFanSpeed Test"
curl -H "Content-Type: application/json" -X GET -d '{"dRackId":"0","dBoxId":"1"}' http://localhost:5001/api/dbox/fanspeed

echo "DboxPing Test"
curl -H "Content-Type: application/json" -X GET -d '{"dRackId":"0","dBoxId":"1"}' http://localhost:5001/api/dbox/ping


echo "DBox Test Completed Successfuly"



echo "Testing DBrick"

echo "DbrickSwitchOn Test"
curl -H "Content-Type: application/json" -X POST -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}' http://localhost:5001/api/dbrick/switchon

echo "DbrickSwitchOff Test"
curl -H "Content-Type: application/json"  -X POST -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}' http://localhost:5001/api/dbrick/switchoff

echo "DbrickIsOn Test"
curl -H "Content-Type: application/json"  -X GET -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}' http://localhost:5001/api/dbrick/ison

echo "Dbrick Test"
curl -H "Content-Type: application/json"  -X GET -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}' http://localhost:5001/api/dbrick/info

echo "DbrickPower Test"
curl -H "Content-Type: application/json"  -X GET -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}' http://localhost:5001/api/dbrick/power

echo "DbrickGetBootSource Test"
curl -H "Content-Type: application/json"  -X GET -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}' http://localhost:5001/api/dbrick/getbootsource

echo "DbrickSetBootSource Test"
curl -H "Content-Type: application/json"  -X POST -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11","path":"/dev/sda"}' http://localhost:5001/api/dbrick/setbootsource

echo "DbrickLinks Test"
curl -H "Content-Type: application/json"  -X GET -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}' http://localhost:5001/api/dbrick/links

echo "DbrickPing Test"
curl -H "Content-Type: application/json"  -X GET -d '{"dRackId":"0","dBoxId":"1","dBrickId":"11"}' http://localhost:5001/api/dbrick/ping


echo "DBrick Test Completed Successfuly"



echo "Testing RemoteMemory"

echo "AddRemoteMemory Test"
curl -H "Content-Type: application/json" -X POST -d '{"memoryAddress":[{"startA":"0x41000000","endA":"0x430000000","port":21,"offset":45,"action":"Add"},{"startA":"0x45000000","endA":"0x470000000","port":21,"offset":45,"action":"Add"},{"startA":"0x48000000","endA":"0x530000000","port":21,"offset":45,"action":"Add"}]}' http://0.0.0.0:5001/api/memory/addremotememory

echo "RemoveRemoteMemory Test"
curl -H "Content-Type: application/json" -X POST -d '{"memoryAddress":[{"startA":"0x41000000","endA":"0x430000000","port":21,"offset":45,"action":"Remove"},{"startA":"0x45000000","endA":"0x470000000","port":21,"offset":45,"action":"Remove"},{"startA":"0x48000000","endA":"0x530000000","port":21,"offset":45,"action":"Remove"}]}' http://0.0.0.0:5001/api/memory/removeremotememory

echo "Memory Test Completed Successfuly"
echo "Test Script Completed!!"
