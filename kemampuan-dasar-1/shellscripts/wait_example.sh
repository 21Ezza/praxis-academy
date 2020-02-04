echo "wait command" &
prcess_id=$!
wait $process_id
echo "Exit status $?"
