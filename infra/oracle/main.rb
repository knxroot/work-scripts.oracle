#!/usr/bin/env ruby

$d_diagno = Diagno.new('env/dev')
$l_diagno = Diagno.new('env/local')
$vagrant = Vagrant.new
$d_install = Install.new('env/dev')
$l_install = Install.new('env/local')
$m_dg = Oradg.new('env/localhost')
