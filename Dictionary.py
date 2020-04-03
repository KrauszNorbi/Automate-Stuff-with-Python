import pprint #pretty print

message = 'A practical programming course for office workers.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count [character] = count[character] + 1

pprint.pprint(count)
