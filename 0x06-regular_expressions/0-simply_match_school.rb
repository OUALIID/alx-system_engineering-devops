#!/usr/bin/env ruby
"""
This code searches the input string for all occurrences of the word `school` exactly.
                    ==> puts ARGV[0].scan(/School/).join <==
The `join` method combines all the elements of the array(result of `scan`) into a single string, with no separator between them.
"""
puts ARGV[0].scan(/School/)