# importing a single name
from sales_tax import add_sales_tax

def print_receipt():
    total = ...
    state = ...
    
    print(f'TOTAL: {total}')
    print(f'AFTER TAX: {add_sales_tax(total, state)}')
    
    
    
    
###### formas de import #######
from sales_tax import add_sales_tax, add_state_tax, add_city_tax, add_local_millage_tax

from sales_tax import {
    add_sales_tax,
    add_state_tax,
    add_city_tax,
    add_local_millage_tax
}

import sales_tax

###############################