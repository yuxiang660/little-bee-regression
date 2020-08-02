echo 'start model'
sleep 5
echo 'TCP HOST:hsv-sc21 PORT:8085' > data/socket_port.info
n=1
while [ $n -le 10 ]
do
    cat data/socket_port.info
    sleep 3
    n=$(( n+1 ))
done
