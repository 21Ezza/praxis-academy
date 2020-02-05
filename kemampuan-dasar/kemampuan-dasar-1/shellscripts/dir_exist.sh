echo -n "Enter dir name : "
read nDir

if [ -d "$nDir" ]
then
echo "Folder Exist"
else
`mkdir $nDir`
echo "Folder $nDir created"
fi
