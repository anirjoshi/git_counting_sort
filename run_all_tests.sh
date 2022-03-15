#$1 is the file name to run
#$2 test cases dir
#$3 output file
echo -n "">$3
for i in $(ls ./$2|sort -r);
do
	
	#echo $i
	nos=$(echo $i|cut -d "_" -f 3| cut -d "." -f 1)
	echo $nos
	python $1 $2/$i $nos>> $3
done
