"""
Challenge #069  [Easy] pretty list.

Description

Write a program that takes a title and a list as input and outputs the list in 
a nice column. Try to make it so the title is centered. For example:

title: 'Necessities'

input: ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls']

output:

    +---------------+
    |  Necessities  |
    +---------------+
    | fairy         |
    | cakes         |
    | happy         |
    | fish          |
    | disgustipated |
    | melon-balls   |
    +---------------+


Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

def print_seperator_line(output,length):
  output = output + '+-' + ('-' * length) + '-+\n'
  return output

def print_list(title,list):
  output = ''
  max_length = 0

  for i in list:
    if len(i) > max_length:
      max_length = len(i)

  if len(title) > max_length:
    max_length = len(title)

  padding = max_length - len(title)
  output = print_seperator_line(output,max_length)
  output = output + '| ' + (' ' * (padding / 2)) + title + (' ' * (padding - (padding /2))) + ' |\n'
  output = print_seperator_line(output,max_length)

  for i in list:
    padding = max_length - len(i)
    output = output + '| ' + i + (' ' * padding) + ' |\n'

  output = print_seperator_line(output,max_length)

  return output
