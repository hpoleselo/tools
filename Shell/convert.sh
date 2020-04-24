# Receives the file and renames it to the wished/input name
mv {$1,$2.bag}

# Generates the csv file
rostopic echo -b $2.bag -p /printer3d > $2.csv

