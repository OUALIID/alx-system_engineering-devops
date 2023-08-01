#!/usr/bin/env ruby
"""
The code searches for occurrences of specific patterns in the first command-line argument (ARGV[0])
that follow the format'[from: ...] [to: ...] [flags: ...]',and then it prints the captured substrings
for each pattern as a single concatenated string without any separator.

`\]\ \[\`: Matches the literal sequence '] [' (closing square bracket followed by a space and then an opening square bracket).

`(.*?)`: This is a non-greedy capture group. It captures any characters (except newline characters) zero or more times,
but it does so non-greedily, meaning it captures as few characters as possible to make the whole pattern match.
This allows the capture group to match everything inside the square brackets.

                        ==> puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join <==
The `join` method combines all the elements of the array(result of `scan`) into a single string, with no separator between them.
"""
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join