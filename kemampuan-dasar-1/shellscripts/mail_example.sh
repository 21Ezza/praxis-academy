sendTo="barnando13@gmail.com"
subject="test"
msg="Hello World from Bash"
`mail -s $subject $sendTo <<< $msg`

