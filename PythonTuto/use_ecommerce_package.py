# import all the Module
import ecommerce.shipping

# call a function inside a module of package
ecommerce.shipping.calc_shipping()

# another way
from ecommerce import shipping

# call function ofo module
shipping.calc_shipping()

# import a module from a package
from ecommerce.shipping import calc_shipping

# call a function from module of ecommerce

calc_shipping()