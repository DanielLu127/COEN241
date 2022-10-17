#! /bin/bash
echo "File IO Test"
for value in {1..5}
do 
	echo "Try" $value
	sysbench --num-threads=8 --test=fileio --file-total-size=2G --file-test-mode=rndrw prepare
	sysbench --num-threads=8 --test=fileio --file-total-size=2G --file-test-mode=rndrw run
	sysbench --num-threads=8 --test=fileio --file-total-size=2G --file-test-mode=rndrw cleanup
done 