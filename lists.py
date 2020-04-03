supplies = ['pens', 'staplers', 'binders', 'tapes']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


# multiple assignment
cat =  ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

size, color, disposition = cat

size, color, disposition = 'skinny', 'black', 'quiet'

#swapping vatiables
a = 'AAA'
b = 'BBB'
a, b = b, a

spam = 42
spam = spam + 1
spam += 1
spam
