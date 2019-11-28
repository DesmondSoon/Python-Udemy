"""

This script is to understand the build in function __name__ == __main__

This function checks if you are currently running this script directly.

With this we can access if statements when its the __main__
We know then we are running this script directly



"""



def func():
    print('Func() IN ONE.PY')

print("Top LEVEL IN ONE.PY")


if __name__ == '__main__':
    print('One.PY is being run directly')
else:
    print('One.PY is being imported')
