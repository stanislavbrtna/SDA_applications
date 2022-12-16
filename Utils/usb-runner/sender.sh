#!/bin/bash
INPUT="$1"
#set the terminal parameters
stty 0:4:cbd:8a30:3:1c:7f:15:4:64:1:0:11:13:1a:0:12:f:17:16:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0:0 -F /dev/ttyUSB0

SIZE=$( stat --printf="%s" $1)
NAME=$( basename $1)

#send file size and name
printf "Sending %s (%s bytes)\n" $NAME $SIZE 
printf "TRANSMIT!N:%s!S:%s!\n" $NAME $SIZE  > /dev/ttyUSB0
sleep 0.7

# sending file
while IFS= read -r line
do
	printf "%s\n" "$line" > /dev/ttyUSB0
	printf "."
	sleep 0.001
done < "$INPUT"
printf "\nDone\n"
