#!/bin/csh

echo 'start model'
sleep 5
mkdir -p data
echo 'TCP HOST:hsv-sc21 PORT:8085' > data/socket_port.info
set i=1
while ($i < 10)
    cat data/socket_port.info
    sleep 3
    @ i++
end
