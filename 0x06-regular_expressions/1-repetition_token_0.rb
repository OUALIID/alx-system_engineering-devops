#!/usr/bin/env ruby
"""
The code searches for occurrences of the pattern `hbt` followed by 2 to 5 occurrences of the letter
't' and ending with the letter 'n' in the first command-line argument (ARGV[0]).

                        ==> puts ARGV[0].scan(/School/).join <==
The `join` method combines all the elements of the array(result of `scan`) into a single string, with no separator between them.
"""
puts ARGV[0].scan(/hbt{2,5}n/)