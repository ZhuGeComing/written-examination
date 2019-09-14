result = ''
with open('123.txt', 'r') as f:
    s = f.read()
    for i in s:
        if(i == '\n'):
            result = result+i+'~|'
        else:
            result = result+i+'|'
with open('888.txt', 'w') as f:
    f.write(result[:-1])
