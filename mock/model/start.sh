echo 'start model'
sleep 5
echo 'TCP HOST:hsv-sc21 PORT:8085' > data/socket_port.info
while true; do
    cat data/socket_port.info
    sleep 3
done
