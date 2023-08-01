#!/usr/bin/env ruby
"""
The code searches for occurrences of the pattern 'hb', followed by an optional 't',
and ending with an optional 'n' in the first command-line argument (ARGV[0]),
and then it prints the matched substrings as a single concatenated string without any separator.

                        ==> puts ARGV[0].scan(/hb?t?n/).join <==
The `join` method combines all the elements of the array(result of `scan`) into a single string, with no separator between them.
"""
puts ARGV[0].scan(/hb?t?n/)