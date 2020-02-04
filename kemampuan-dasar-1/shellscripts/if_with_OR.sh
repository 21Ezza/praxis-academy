echo -n "Enter any Number : "
read n

if [[ ( $n -eq 15 || $n -eq 45 ) ]]
then
echo -e "You won the game"
else
echo -e "You lost"
fi
