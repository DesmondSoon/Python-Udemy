

'''
This exercises is for understanding Methods and Packages.

Allowing transperancy without clogging up scripts.

__init__ allows Python to understand that inside the package contains modules

Pipfile is a VE virtual enviroment where i can store settings
'''


from mymodule import my_func
from MyMainPackage import some_main_script
from MyMainPackage.MySubPackage import my_subscript


my_func()
some_main_script.report_main()
my_subscript.sub_report()
