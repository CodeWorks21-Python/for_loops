# Simple for loop

print('simple loop')
for i in range(10):
    print(i)


# range() variations
#   - range(stop)
#   - range(start, stop)
#   - range(start, stop, step)

stop = 15

print(f'\nstop = {stop}')

for i in range(stop):
    print(i)


start = 5
stop = 15

print(f'\nstart = {start}, stop = {stop}')

for i in range(start, stop):
    print(i)


start = 5
stop = 15
step = 3

print(f'\nstart = {start}, stop = {stop}, step = {step}')

for i in range(start, stop, step):
    print(i)


# If you want to go backwards, your step must be negative, and your start must be greater than stop.
start = 10
stop = -5
step = -1

print(f'\nstart = {start}, stop = {stop}, step = {step}')

for i in range(start, stop, step):
    print(i)


# Direct Access

print()
text = 'Here is some text. Remember that a string is a sequence!'
for char in text:
    print(char)


# You can also use in range() to access the string by using the iterator variable as the position.

print()
text = input('lets get user input this time' + '\n' + 'please enter your name: ')
for i in range(len(text)):
    print(text[i])


# Run a for loop, 10 to 50, but step by 5

# range(stop)
# range(start, stop)
# range(start, stop, step)

# s --> number of symbols, sp --> spaces

# ***** | s = i | sp = 0 --> sp = start - i
#  **** | s = i | sp = 1 --> sp = start - i
#   *** | s = i | sp = 2 --> sp = start - i
#    ** | s = i | sp = 3 --> sp = start - i
#     * | s = i | sp = 4 --> sp = start - i

start = 10
stop = 0
print()
for i in range(start, stop, -1):
    print(' ' * (start - i) + '$' * i)


# s --> number of symbols, sp --> number of spaces

#     $ | i = 1 | s = 1, s = i | sp = 4, sp = stop - i - 1
#    $$ | i = 2 | s = 2, s = i | sp = 3, sp = stop - i - 1
#   $$$ | i = 3 | s = 3, s = i | sp = 2, sp = stop - i - 1
#  $$$$ | i = 4 | s = 4, s = i | sp = 1, sp = stop - i - 1
# $$$$$ | i = 5 | s = 5, s = i | sp = 0, sp = stop - i - 1

# range(1, 6, 1)

start = 1
stop = 6
print()
for i in range(start, stop, 1):
    print(' ' * (stop - i - 1) + '$' * i)










