#!/usr/bin/env ruby
"""
The code searches for and extracts all occurrences of consecutive uppercase letters in the first command-line argument (ARGV[0]),
and then it prints the matched substrings as a single concatenated string without any separator.

`[A-Z]`: This is a character class that matches any uppercase letter from 'A' to 'Z'.

`+`: The plus sign '+' is a quantifier in regular expressions. It means 'one or more occurrences of the preceding character or character class.'

                        ==> puts ARGV[0].scan(/[A-Z]+).join <==
The `join` method combines all the elements of the array(result of `scan`) into a single string, with no separator between them.
"""
puts ARGV[0].scan(/[A-Z]+/).join