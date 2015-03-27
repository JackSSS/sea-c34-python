def path():
    """Is it possible to print a directory?"""

    from os import directory


    path = "./directory"
    for i in directory(path):
        print(i)

path()
# I know this isn't ideal for obvious reasons but wanted to try.
# There was no memory hurt in the making of this function.
