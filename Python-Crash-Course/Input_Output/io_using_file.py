poem = '''\
    programming is fun
    when the work is done
    If you wanna make your work also fun:
    use Python!
    '''

# Open for Writing
f = open('poem.txt', 'w')
# Write text to a file
f.write(poem)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close()