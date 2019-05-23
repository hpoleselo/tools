# Receives the file and renames it to the wished/input name
mv {$1,$2.bag}

# Generates the csv format
rostopic echo -b $2.bag -p /printer3d

