f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()

f.write('This is a test')

f.readline()