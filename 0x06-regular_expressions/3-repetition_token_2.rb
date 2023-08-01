#!/usr/bin/env ruby
"""
The code searches for occurrences of the pattern 'hbt', followed by one or more occurrences of the letter 't',
in the first command-line argument (ARGV[0]), and then it prints the matched substrings as an array.

`+`: `+`: The plus sign (+) is a quantifier in regular expressions. It means 'one or more occurrences of the preceding character.'
In this case, the preceding character is 't'.

                        ==> puts ARGV[0].scan(/hbt+n/).join <==
The `join` method combines all the elements of the array(result of `scan`) into a single string, with no separator between them.
"""
puts ARGV[0].scan(/hbt+n/)
