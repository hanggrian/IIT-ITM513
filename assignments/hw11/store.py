"""
Assignment #11
Represent restaurant and grocery store as objects with shared attributes.

Author: Hendra Wijaya (A20529195)
"""

from abc import ABC, abstractmethod

STATUS_OPEN = 'open'
STATUS_CLOSED = 'closed'


class Store(ABC):
    """Superclass of restaurant and grocery store."""

    def __init__(
        self,
        name: str,
        address: str,
        status: str,
        sales_tax_pct: float,
    ):
        """
        The main constructor.

        :param name: store name, cannot be empty.
        :param address: location, cannot be empty.
        :param status: closed or open, cannot be empty.
        :param sales_tax_pct: percentage of sales tax, cannot be negative.
        """
        if not name or not address:
            raise ValueError('Name and address cannot be empty.')
        if status not in (STATUS_OPEN, STATUS_CLOSED):
            raise ValueError('Unknown status.')
        if sales_tax_pct < 0:
            raise ValueError('Sales tax percentage cannot be negative.')
        self._name = name
        self._address = address
        self._status = status
        self._sales_tax_pct = sales_tax_pct

    @property
    def name(self) -> str:
        """
        :return: store name.
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        :param name: store name, cannot be empty.
        """
        if not name:
            raise ValueError('Name cannot be empty.')
        self._name = name

    @property
    def address(self) -> str:
        """
        :return: location.
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        :param address: location, cannot be empty.
        """
        if not address:
            raise ValueError('Address cannot be empty.')
        self._address = address

    @property
    def status(self) -> str:
        """
        :return: closed or open.
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        :param status: closed or open, cannot be empty.
        """
        if status not in (STATUS_OPEN, STATUS_CLOSED):
            raise ValueError('Unknown status.')
        self._status = status

    @property
    def sales_tax_pct(self) -> float:
        """
        :return: percentage of sales tax.
        """
        return self._sales_tax_pct

    @sales_tax_pct.setter
    def sales_tax_pct(self, sales_tax_pct: float) -> None:
        """
        :param sales_tax_pct: percentage of sales tax, cannot be negative.
        """
        if sales_tax_pct < 0:
            raise ValueError('Sales tax percentage cannot be negative.')
        self._sales_tax_pct = sales_tax_pct

    def is_store_open(self) -> bool:
        """Returns true if store is open."""
        return self.status == STATUS_OPEN

    @abstractmethod
    def calculate_total_sales_tax(self) -> float:
        """Returns tax of total sales."""

    @abstractmethod
    def calculate_total_sales(self) -> float:
        """Returns total sales."""
