#!/usr/bin/env ruby
# A ruby script tthat accepts one arg and pass it to regex
puts ARGV[0].scan(/School/).join.chomp
