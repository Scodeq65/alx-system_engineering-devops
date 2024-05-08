#!/usr/bin/env ruby

# This script accepts one argument and passes it to a regular expression matching method.
# The regular expression matches strings that start with "h", followed by any single character (represented by "."), and end with "n".
puts ARGV[0].scan(/^h.n$/).join
