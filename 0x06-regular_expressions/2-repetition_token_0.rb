#!/usr/bin/env ruby
# This script accepts one argument and matches the pattern "htn" or "hbtn" in it.
puts ARGV[0].scan(/hb{0,1}tn/).join

