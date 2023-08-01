#!/usr/bin/env ruby
"""
The regular expression `/^h.n$/` matches substrings that start with 'h', followed by any single character, and end with 'n'.

`^`: The caret symbol '^' is an anchor that denotes the start of a line. It means the pattern should start with the character 'h'
at the beginning of the string.

`.`: The dot '.' is a special character in regular expressions that matches any single character (except newline characters).

`$`: The dollar sign '$' is an anchor that denotes the end of a line. It means the pattern should end with the character 'n'
at the end of the string.

                        ==> puts ARGV[0].scan(/^h.n$/).join <==
The `join` method combines all the elements of the array(result of `scan`) into a single string, with no separator between them.
"""
puts ARGV[0].scan(/^h.n$/)