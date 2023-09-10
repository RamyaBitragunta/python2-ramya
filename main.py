# if we want to use functions (present in operations.py) from the main module
# so we can access these functions from the main module in three diff ways.

# approach-1

# we have to import operations module, once we have imported this module, we can call those functions
# -directly by using these modules

import operations

operations.add(10,20)
operations.mul(10,20)

# we can import this module by using import key word and by using this module name directly we can access these functions
# in this approach suppose if we want to call all the functions ., we need to specify the module name
# suppose if we dont want to call this module name evrytime bt want to call functions we have an another approach

# approach-2

from operations import add,mul
add(10,20)
mul(10,20)

# as we can see here, in second approach we have only 2 functions, that we can specify here.
# if we have n no.of functions in a module, in this approach we have specify each and evry fntn by keeping comma in b/w
# instead of this we can just put *(star)- it will import each and evry function


# approach-3

from operations import *
add(10,20)
mul(30,40)




