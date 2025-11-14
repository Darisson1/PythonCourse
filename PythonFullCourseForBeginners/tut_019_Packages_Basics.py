
import ecommerce.shipping

ecommerce.shipping.calc_shipping()


#or, when no prefix import single functions from module in the package
from ecommerce.shipping import calc_shipping, calc_total_cost
calc_shipping()
calc_total_cost()

#or, when no prefix import ALL functions from the module in the package, so the whole module
from ecommerce.shipping import shipping
shipping.calc_shipping()
shipping.calc_total_cost()
