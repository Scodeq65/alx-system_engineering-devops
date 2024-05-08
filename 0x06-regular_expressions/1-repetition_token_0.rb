#!/usr/bin/env ruby
# script accept one arg and matches it with the pattern "hbt{2,5}n"
puts ARGV[0].scan(/hbt{2,5}n/).join
