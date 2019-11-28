"""

This script is to understand the build in function __name__ == __main__

This function checks if you are currently running this script directly.

With this we can access if statements when its the __main__
We know then we are running this script directly



"""

import one


print("Top LEVEL IN TWO.PY")
one.func()

if __name__ == '__main__':
    print('Two.PY is being run directly')
else:
    print('Two.PY is being imported')
