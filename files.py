file =  open('test.py', 'x')
file.write('Testing creating py file.')
file.close()

#file = open('test.py', 'w')
#file.write('Overwrite existing file')
#file.close()

file = open('test.py', 'a')
file.write(' Added to the end of existing file.')
file.close()
