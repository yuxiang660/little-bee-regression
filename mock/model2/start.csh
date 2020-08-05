#!/bin/csh

echo 'start model2'
sleep 5
mkdir -p data
echo 'TCP HOST:model2 PORT:8888' > data/socket_port.info
set i=1
while ($i < 10)
    cat data/socket_port.info
    sleep 3
    @ i++
end
