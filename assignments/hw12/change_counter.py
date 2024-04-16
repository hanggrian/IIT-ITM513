"""
Assignment #12
Recursion and single-window GUI application wrapped in a main method.

Author: Hendra Wijaya (A20529195)
"""

from tkinter import Tk, Frame, Label, Entry, Button, GROOVE, E, N, S, W

FONT_BODY = ('Noto Sans', 12)
FONT_BODY_RAISED = ('Noto Sans', 12, 'bold')
FONT_INPUT = ('Noto Sans Mono', 12)
FONT_INPUT_RAISED = ('Noto Sans Mono', 14, 'bold')
FONT_BUTTON = ('Noto Sans', 14)

PADDING_SMALL = 5
PADDING_LARGE = 20

input_count: int = 0
output_count: int = 0


class Coin:
    """Object class representing cash amount in selected currency."""

    DOLLAR = 'dollar'
    QUARTER = 'quarter'
    DIME = 'dime'
    NICKEL = 'nickel'
    PENNY = 'penny'

    def __init__(self, coin_type, amount):
        """
        Main constructor.

        :param coin_type: currency type, one of the declared types.
        :param amount: cash value, cannot be negative.
        """
        if coin_type not in (Coin.DOLLAR, Coin.QUARTER, Coin.DIME, Coin.NICKEL, Coin.PENNY):
            raise ValueError('Unknown coin type.')
        if amount < 0:
            raise ValueError('Coin amount cannot be negative.')
        self._coin_type = coin_type
        self._amount = amount

    @property
    def coin_type(self):
        """
        :return: currency type.
        """
        return self._coin_type

    @coin_type.setter
    def coin_type(self, coin_type):
        """
        :param coin_type: currency type, one of the declared types.
        """
        if coin_type not in (Coin.DOLLAR, Coin.QUARTER, Coin.DIME, Coin.NICKEL, Coin.PENNY):
            raise ValueError('Unknown coin type.')
        self._coin_type = coin_type

    @property
    def amount(self):
        """
        :return: cash amount.
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        :param amount: cash amount, cannot be negative.
        """
        if amount < 0:
            raise ValueError('Coin amount cannot be negative.')
        self._amount = amount

    @property
    def dollar_amount(self):
        """
        :return: cash value in a converted dollar amount.
        """
        match self._coin_type:
            case Coin.QUARTER:
                return self._amount * 0.25
            case Coin.DIME:
                return self._amount * 0.1
            case Coin.NICKEL:
                return self._amount * 0.05
            case Coin.PENNY:
                return self._amount * 0.01
            case _:
                return self._amount


def parse_input(entry):
    """
    Retrieve numerical value from GUI text field.

    :param entry: input field.
    :return: numerical value.
    """
    text = entry.get()
    if not text:
        return 0
    try:
        value = int(text)
        if value >= 0:
            return value
        return 0
    except ValueError:
        return 0


def update_output(entry, label, value):
    """
    Modify output label state text and text color based on input value.

    :param entry: input field.
    :param label: output display.
    :param value: cash amount in dollar.
    :return:
    """
    if entry is None or not entry.get():
        color = '#000'
    elif value == 0:
        color = '#b00020'
    else:
        color = '#09af00'
    label.config(text=f' {value:.2f} ', fg=color)


def main():
    """The main function."""

    def add_input_line(label_text):
        global input_count  # pylint: disable=invalid-name, global-statement
        input_count += 1

        Label(root, text=f'{label_text}:', font=FONT_BODY).grid(
            row=input_count,
            column=0,
            padx=PADDING_SMALL,
            pady=PADDING_SMALL,
            sticky=E,
        )

        entry = Entry(root, font=FONT_INPUT)
        entry.bind('<Return>', calculate)
        entry.grid(
            row=input_count,
            column=1,
            padx=PADDING_SMALL,
            pady=PADDING_SMALL,
            sticky=N + S + W + E,
        )
        root.columnconfigure(1, weight=1)
        return entry

    def add_output_line(label_text):
        global output_count  # pylint: disable=invalid-name, global-statement
        output_count += 1
        if output_count < 5:
            font1 = FONT_BODY
            font2 = FONT_INPUT
        else:
            font1 = FONT_BODY_RAISED
            font2 = FONT_INPUT_RAISED

        Label(root, text=f'{label_text}: $', font=font1).grid(
            row=output_count,
            column=3,
            padx=(PADDING_LARGE, PADDING_SMALL),
            pady=PADDING_SMALL,
            sticky=E,
        )

        label = Label(root, text=' 0.00 ', font=font2, relief=GROOVE, borderwidth=2, anchor=E)
        label.grid(
            row=output_count,
            column=4,
            padx=PADDING_SMALL,
            pady=PADDING_SMALL,
            sticky=N + S + W + E,
        )
        return label

    def calculate(_=None):
        quarter_in_dollar = Coin(Coin.QUARTER, parse_input(quarter_entry)).dollar_amount
        dime_in_dollar = Coin(Coin.DIME, parse_input(dime_entry)).dollar_amount
        nickel_in_dollar = Coin(Coin.NICKEL, parse_input(nickel_entry)).dollar_amount
        penny_in_dollar = Coin(Coin.PENNY, parse_input(penny_entry)).dollar_amount
        total_in_dollar = quarter_in_dollar + dime_in_dollar + nickel_in_dollar + penny_in_dollar

        update_output(quarter_entry, quarter_label, quarter_in_dollar)
        update_output(dime_entry, dime_label, dime_in_dollar)
        update_output(nickel_entry, nickel_label, nickel_in_dollar)
        update_output(penny_entry, penny_label, penny_in_dollar)
        update_output(None, total_label, total_in_dollar)

    window = Tk()
    window.title('Change Counter')
    window.minsize(480, False)
    window.maxsize(1280, False)
    window.resizable(True, False)
    window.columnconfigure(0, weight=1)

    root = Frame(window)
    root.grid(padx=PADDING_LARGE, pady=PADDING_LARGE, sticky=N + S + E + W)

    Label(root, text='Enter the number of each coin type and hit, Compute:', font=FONT_BODY).grid(
        row=0,
        column=0,
        columnspan=4,
        pady=(0, PADDING_LARGE),
        sticky=W,
    )

    quarter_entry = add_input_line('Quarters')
    dime_entry = add_input_line('Dimes')
    nickel_entry = add_input_line('Nickels')
    penny_entry = add_input_line('Pennies')

    quarter_label = add_output_line('Quarter value')
    dime_label = add_output_line('Dime value')
    nickel_label = add_output_line('Nickel value')
    penny_label = add_output_line('Penny value')
    total_label = add_output_line('Total change value')

    button = Button(root, text='Compute', font=FONT_BUTTON, command=calculate)
    button.grid(
        row=5,
        column=0,
        columnspan=2,
        padx=PADDING_SMALL,
        pady=PADDING_SMALL,
        sticky=N + S + E + W,
    )

    window.mainloop()


if __name__ == "__main__":
    main()
