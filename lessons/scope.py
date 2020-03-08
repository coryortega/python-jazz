my_name = 'bill'

def print_name():
    global my_name
    my_name = 'JIM'
    print('the name inside the function, ', my_name)

print_name()
print('outside the function the name is ', my_name)