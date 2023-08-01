#!/usr/bin/env ruby
"""
The code searches for and extracts all occurrences of a 10-digit number at the beginning of the first command-line argument (ARGV[0]),
then prints the matched substrings as an array.

`^`: The caret symbol '^' is an anchor that denotes the start of a line. It means the pattern should start at the beginning of the string.

`\d`: The backslash followed by 'd' represents a digit character in regular expressions, matching any numeric digit (0-9).

`{10}`: The curly braces '{}' denote a quantifier, and in this case, it means the preceding pattern (the digit '\d') should appear exactly 10 times.

                        ==> puts ARGV[0].scan(/^\d{10}/).join <==
The `join` method combines all the elements of the array(result of `scan`) into a single string, with no separator between them.
"""
puts ARGV[0].scan(/^\d{10}/)