# !/bin/bash
echo "Test case: prime number = 30000"
for vslue in {1..5}
do 
	echo "Try: " $value
	sysbench --test=cpu --cpu-max-prime=30000 --time=10 run
done 