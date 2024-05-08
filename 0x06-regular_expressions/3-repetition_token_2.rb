#!/usr/bin/env ruby
# This script accepts one argument and matches the pattern "htn" or "hbtn" in it.
puts ARGV[0].scan(/hbt{1,4}n/).join

