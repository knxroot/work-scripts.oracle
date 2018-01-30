find -L . -path '*/src/*/*.xml'|xargs -i ack 'insert into (\w+)' {} --output='$1'|sort -u
