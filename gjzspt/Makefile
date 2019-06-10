SHELL:=/usr/bin/zsh

all:

gen: dataclean.sql.jsonnet
	jsonnet -m gen -S dataclean.sql.jsonnet

clean:
	rm -rf gen/*
	

.PHONY: all gen clean
