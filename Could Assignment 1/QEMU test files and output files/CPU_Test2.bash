# !/bin/bash
echo "Test case: prime number = 10000"
for vslue in {1..5}
do 
	echo "Try: " $value
	sysbench --test=cpu --cpu-max-prime=10000 --time=10 run
done 