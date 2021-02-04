# import a module
import define_module

print(define_module.lbs_to_kg(160))
print(define_module.kg_to_lbs(70))

# import a function from module
from define_module import kg_to_lbs

# call it without prefix
print(kg_to_lbs(78))


