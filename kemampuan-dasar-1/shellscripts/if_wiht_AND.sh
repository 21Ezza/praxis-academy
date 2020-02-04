echo -n "> Enter Username : "
read username
echo -n "> Enter Password : "
read password

if [[ ($username == "admin" && $password == "secret") ]]
then
echo "valid user"
else
echo "invalid User"
fi
