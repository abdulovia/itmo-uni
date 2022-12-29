#!/bin/bash

solve() {
	divz=$(($a/$b))
	div1=$(($a*10/$b%10))
	div2=$(($a*100/$b%10))
	if [[ $1 -eq 0 ]]
	then
		echo "$sum $dif $mlt -$divz.$div1$div2"
	else
		echo "$sum $dif $mlt $divz.$div1$div2"
	fi
}

a=$1
b=$2
sum=$(($a+$b))
dif=$(($a-$b))
mlt=$(($a*$b))
if [[ $b -eq 0 ]] 
then
	echo "$sum $dif $mlt #"
else
	if [[ $mlt < 0 ]]
	then
		if [[ $a < 0 ]]
		then
			a=$(( $a * (-1) ))
		else
			b=$(( $b * (-1) ))
		fi
		solve 0
	else
		solve 1
	fi
fi
