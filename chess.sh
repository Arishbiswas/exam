#!/bin/bash

if [ $# -eq 0 ];
then
echo "no arguments found"
fi

n=$1
echo  $n


for (( j = 0; j<n; j++ ))
do
case $j in
0)
echo -ne "\e[48;5;235m \e[0m" ;;
1)
echo -ne "\e[48;5;255m \e[0m"  ;;
2)
echo -ne "\e[48;5;235m \e[0m" ;;
3)
echo -ne "\e[48;5;255m \e[0m"  ;;
4)
echo -ne "\e[48;5;235m \e[0m"  ;;
5)
echo -ne "\e[48;5;255m \e[0m"  ;;
6)
echo -ne "\e[48;5;235m \e[0m"  ;;
7)
echo -ne "\e[48;5;255m \e[0m"  ;;
esac
done

