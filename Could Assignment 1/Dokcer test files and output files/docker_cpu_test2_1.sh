#! /bin/bash
echo "File IO Test: Docker"
for value in {1..5}
do
	echo "Try" $value
	docker run --rm -m="1g" --cpuset-cpus="0" zyclonite/sysbench --test=cpu --cpu-max-prime=10000 --time=10 run
done
