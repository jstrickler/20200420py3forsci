#!/usr/bin/env python

mary_in = open('DATA/mary.txt')
# ...
mary_in.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n (and other trailing space)
        # print(repr(raw_line))
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    entire_file = mary_in.read()
    print("RAW:")
    print(repr(entire_file))
    print("AS STRING:")
    print(entire_file)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines() # don't use this to read line-by-line
    print(all_lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_no_nl = [line.rstrip() for line in mary_in]
    print(all_lines_no_nl)
print('-' * 60)

with open('DATA/words.txt') as words_in:
    for raw_line in words_in:
        if 'snake' in raw_line:
            line = raw_line.rstrip()
            print(line)
print('-' * 60)


with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line.upper())
print('-' * 60)

