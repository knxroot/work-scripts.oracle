#./shell/db.sh echo exp 192.168.21.249 gjzspt

if [ $1 == '-d' ]; then
	ruby -r ./rb/db.rb -e '$dry_run.imp "192.168.21.243","oracle","oracle","oracle","gjzspt","gjzspt","./dmpfiles/gjzspt2016-12-23_nd.dmp"'
else
	ruby -r ./rb/db.rb -e '$run.imp "192.168.21.243","oracle","oracle","oracle","gjzspt","gjzspt","./dmpfiles/gjzspt2016-12-23_nd.dmp"'
fi
