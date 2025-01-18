def make_shirt(size='large', message='I love Python'):
    print(f"The shirt size is {size} and the message on it is '{message}'.")

# Calling the function using positional arguments
make_shirt('medium', 'Hello World')

# Calling the function using keyword arguments
make_shirt(size='small', message='Python is awesome')

# Making a large shirt with the default message
make_shirt()

# Making a medium shirt with the default message
make_shirt(size='medium')

# Making a shirt of any size with a different message
make_shirt(size='small', message='Custom Message')