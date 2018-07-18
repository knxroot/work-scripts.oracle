SHELL:=/usr/bin/zsh

copy-ws-log:
	cat copy-ws-log.sc | spksh --packages oracle.ojdbc:ojdbc:6
