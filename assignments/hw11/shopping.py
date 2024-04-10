"""
Assignment #11
Represent restaurant and grocery store as objects with shared attributes.

Author: Hendra Wijaya (A20529195)
"""

from grocery_store import GroceryStore
from restaurant import Restaurant

END = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[32m'


def report_sales(store):
    """Print sales and sales tax of current store."""
    print('Total sales:', f'{GREEN}${store.calculate_total_sales()}{END}')
    print('Total sales tax:', f'{GREEN}${store.calculate_total_sales_tax()}{END}')


restaurant = Restaurant("Joey G's Mac n Cheese", '959 N Western Ave', 30, 20)

print()
print(
    f'{BOLD}30 people are visiting the restaurant.',
    f'25 served, each paying $20.{END}',
)
print()
print('Is the restaurant open?', f'{GREEN}{restaurant.is_store_open()}{END}')
print('Seating 30 patrons:', f'{GREEN}{restaurant.seat_patrons(30)}{END}')
print('Current occupancy after seating:', f'{GREEN}{restaurant.current_occupancy}{END}')
print('Serving 25 patrons:', f'{GREEN}{restaurant.serve_patrons(25)}{END}')
print('Checkout 20 patrons:', f'{GREEN}{restaurant.checkout_patrons(20)} remaining{END}')
print('Current occupancy after checkout:', f'{GREEN}{restaurant.current_occupancy}{END}')
report_sales(restaurant)

grocery = GroceryStore('Jewel-Osco', '550 N State St')

print()
print(f'{BOLD}Selling 5 of $1 items and 10 of $2.5 items.{END}')
print()
print('Sold 5 items at $1 each:', f'{GREEN}${grocery.sell_item(5, 1)}{END}')
print('Sold 10 items at $2.5 each:', f'{GREEN}${grocery.sell_item(10, 2.5)}{END}')
print('Grocery store type:', f'{GREEN}{grocery.store_type}{END}')
report_sales(grocery)

print()
print('Goodbye!')
print()
