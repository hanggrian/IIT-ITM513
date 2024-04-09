"""
Assignment #11
Represent restaurant and grocery store as objects with shared attributes.

Author: Hendra Wijaya (A20529195)
"""

from docstring_inheritance import inherit_numpy_docstring

from store import Store, STATUS_OPEN, STATUS_CLOSED


class Restaurant(Store):
    """Subclass of store that serves foods and beverages."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        name: str,
        address: str,
        max_occupancy: int,
        price_per_person: float,
        status: str = STATUS_OPEN,
        sales_tax_pct: float = 9,  # https://en.wikipedia.org/wiki/Sales_taxes_in_the_United_States
    ):
        """
        Main constructor.

        :param name: store name, cannot be empty.
        :param address: location, cannot be empty.
        :param max_occupancy: seat limit, cannot be negative.
        :param price_per_person: guest fee, cannot be negative.
        :param status: closed or open, cannot be empty.
        :param sales_tax_pct: percentage of sales tax, cannot be negative.
        """
        super().__init__(name, address, status, sales_tax_pct)
        if max_occupancy < 0 or price_per_person < 0:
            raise ValueError('Max occupancy and price per person cannot be negative.')
        self._total_served = 0
        self._max_occupancy = max_occupancy
        self._current_occupancy = 0
        self._price_per_person = price_per_person

    @property
    def max_occupancy(self) -> int:
        """
        :return: seat limit.
        """
        return self._max_occupancy

    @max_occupancy.setter
    def max_occupancy(self, max_occupancy: float) -> None:
        """
        :param max_occupancy: seat limit, cannot be negative.
        """
        if max_occupancy < 0:
            raise ValueError('Max occupancy cannot be negative.')
        self._max_occupancy = max_occupancy

    @property
    def current_occupancy(self) -> int:
        """
        :return: occupied seats.
        """
        return self._current_occupancy

    @property
    def price_per_person(self) -> float:
        """
        :return: guest fee.
        """
        return self._price_per_person

    @price_per_person.setter
    def price_per_person(self, price_per_person: float) -> None:
        """
        :param price_per_person: guest fee, cannot be negative.
        """
        if price_per_person < 0:
            raise ValueError('Price per person cannot be negative.')
        self._price_per_person = price_per_person

    def seat_patrons(self, patrons: int) -> bool:
        """
        Accept guests into seating table, or reject if exceeds restaurant limit.

        :param patrons: number of guests.
        :return: true if guests are seated.
        """
        if patrons <= 0:
            raise ValueError('Patrons must be positive.')
        if self.status == STATUS_CLOSED:
            print('Store is closed.')
            return False
        if patrons > self._max_occupancy - self._current_occupancy:
            print('We are at capacity, we appreciate your patience.')
            return False
        self._current_occupancy += patrons
        print(f'Welcoming {self._who(patrons)} to {self.name}!')
        return True

    def serve_patrons(self, patrons: int) -> int:
        """
        Assist guests with their order, adjusting the value if exceeds restaurant limit.

        :param patrons: number of guests.
        :return: number of guests.
        """
        if patrons <= 0:
            raise ValueError('Patrons must be positive.')
        if patrons > self._current_occupancy:
            patrons = self._current_occupancy
        self._total_served += patrons
        return patrons

    def checkout_patrons(self, patrons: int) -> int:
        """
        Receive payment from guests, adjusting the value if exceeds restaurant limit.

        :param patrons: number of guests.
        :return: occupied seats.
        """
        if patrons <= 0:
            raise ValueError('Patrons must be positive.')
        if patrons > self._current_occupancy:
            patrons = self._current_occupancy
        self._current_occupancy -= patrons
        return self._current_occupancy

    def calculate_total_sales_tax(self) -> float:
        return self._total_served * self.price_per_person * (self._sales_tax_pct / 100)

    def calculate_total_sales(self) -> float:
        return self._total_served * self._price_per_person

    @staticmethod
    def _who(patrons: int) -> str:
        """Describe the number of guests."""
        if patrons == 1:
            return '1 person'
        return f'{patrons} people'


inherit_numpy_docstring(Store.calculate_total_sales.__doc__, Restaurant.calculate_total_sales)
inherit_numpy_docstring(
    Store.calculate_total_sales_tax.__doc__,
    Restaurant.calculate_total_sales_tax,
)
