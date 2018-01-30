#!/bin/bash

#ruby -r ./vgrnt.rb -e 'up'
#irb -r ./diagno.rb -r ./install.rb -r ./roles.rb -r ./vgrnt.rb
options='-r ./diagno.rb -r ./install.rb -r ./roles.rb -r ./vgrnt.rb -r ./dg.rb -r ./main.rb'
#irb $options
pry $options
#ripl $options
