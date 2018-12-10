SHELL:=/usr/bin/zsh

all:

gen:
	jsonnet -m gen -S dataclean.sql.jsonnet

clean:
	rm -rf gen/*
	

.PHONY: all gen clean
