"""
Assignment #11
Represent restaurant and grocery store as objects with shared attributes.

Author: Hendra Wijaya (A20529195)
"""

from docstring_inheritance import inherit_numpy_docstring

from store import Store, STATUS_OPEN, STATUS_CLOSED

TYPE_INDEPENDENT = 'independent'
TYPE_CHAIN = 'chain'


class GroceryStore(Store):
    """Subclass of store that sells various kinds of item."""

    def __init__(
        self,
        name: str,
        address: str,
        status: str = STATUS_OPEN,
        sales_tax_pct: float = 4,  # https://en.wikipedia.org/wiki/Sales_taxes_in_the_United_States
        store_type: str = TYPE_INDEPENDENT,
    ):
        """
        The main constructor.

        :param name: store name, cannot be empty.
        :param address: location, cannot be empty.
        :param status: availability, cannot be empty.
        :param sales_tax_pct: percentage of sales tax, cannot be negative.
        :param store_type: independent or chain, cannot be empty.
        """
        super().__init__(name, address, status, sales_tax_pct)
        if store_type not in (TYPE_INDEPENDENT, TYPE_CHAIN):
            raise ValueError('Unknown store type.')
        self._total_revenue = 0.0
        self._store_type = store_type

    @property
    def store_type(self) -> str:
        """
        :return: independent or chain.
        """
        return self._store_type

    @store_type.setter
    def store_type(self, store_type: str) -> None:
        """
        :param store_type: independent or chain, cannot be empty.
        """
        if store_type not in (TYPE_INDEPENDENT, TYPE_CHAIN):
            raise ValueError('Unknown store type.')
        self._store_type = store_type

    def sell_item(self, qty: int, price: float) -> float:
        """
        Finalize a sale by customer.

        :param qty: number of items.
        :param price: individual value of an item.
        :return: total revenue.
        """
        if qty <= 0 or price <= 0:
            raise ValueError('Quantity and price must be positive.')
        if self.status == STATUS_CLOSED:
            print('Store is closed.')
            return self._total_revenue
        self._total_revenue += qty * price
        return self._total_revenue

    def calculate_total_sales_tax(self) -> float:
        return self._total_revenue * self._sales_tax_pct / 100

    def calculate_total_sales(self) -> float:
        return self._total_revenue


inherit_numpy_docstring(Store.calculate_total_sales.__doc__, GroceryStore.calculate_total_sales)
inherit_numpy_docstring(
    Store.calculate_total_sales_tax.__doc__,
    GroceryStore.calculate_total_sales_tax,
)
