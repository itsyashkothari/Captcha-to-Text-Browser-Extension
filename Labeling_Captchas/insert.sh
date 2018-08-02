cd data
echo "$1"
echo "$2"
if [ ! -d "$1" ]; then    
	mkdir $1
fi;
cp $2 $1
