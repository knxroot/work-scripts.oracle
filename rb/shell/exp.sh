#./shell/db.sh echo exp 192.168.21.249 gjzspt

if [ $1 = '-d' ]; then
	ruby -r ./rb/db.rb -e '$dry_run.exp "192.168.21.249","oracle","oracle","Oe123qwe###","gjzspt","./dmpfiles"'
else
	ruby -r ./rb/db.rb -e '$run.exp "192.168.21.249","oracle","oracle","Oe123qwe###","gjzspt","./dmpfiles"'
fi
