function greeting(){

str="Hello, $name"
echo $str
}

echo -n "Enter name : "
read name

val=$(greeting)
echo "Return value of the funtion is ' $val '"
