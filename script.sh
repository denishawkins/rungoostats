for datafile in *[AB].txt; do
	echo Sdatafile 
	bash goostats "${datafile}" stats-"${datafile"}";
done
