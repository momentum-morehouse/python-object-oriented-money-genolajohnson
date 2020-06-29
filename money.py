# pylint: disable=unidiomatic-typecheck,unnecessary-pass


class DifferentCurrencyError(Exception):
    


 class Currency:
    # """
    # Represents a currency. Does not contain any exchange rate info.
    # """

    def __init__(self, name, code, symbol=None, digits=2):

        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

        # """ class is currency self.name, code, symbol, digits are instances
        # Parameters:
        # - name -- the English name of the currency
        # - code -- the ISO 4217 three-letter code for the currency USD
        # - symbol - optional symbol used to designate currency
        # - digits -- number of significant digits used 2
        # """
        

    def __str__(self):
        if self.symbol:
            return f"{self.code}({self.symbol})
        else:
            return f"{self.code}

        # """  
        # Should return the currency code, or code with symbol in parentheses.
        # """
        # pass

class Name:
    def __eq__(self, other):
        # print("name __eq__ called")

        
        # """All fields must be equal to for the objects to be equal.
        # """


        return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)


class Money:
    # """
    # Represents an amount of money. Requires an amount and a currency.
    # """

    def __init__(self, amount, currency):

        self.amount = amount
        self.currency = currency

        # """
        # Parameters:
        # - amount -- quantity of currency
        # - currency -- type of currency
        # """
        pass

def __str__(self):

# """
        # Should use the currency symbol if available, else use the code.
        # Use the currency digits to determine number of digits to show.
        # """
        # pass

    # self.money = []
    if self.currency.symbol:
            return f"{self.currency.symbol({self.amount}):.{self.currency.digits}f}"
        else:
            return f"{self.currency.code}{self.amount:.{self.currency.digits}f}" 
                

    def __repr__(self):
        # repr formal representation --str__ informal representation
            return f"<Money {str(self)}>"

    def __eq__(self, other):
       
        """
        All fields must be equal to for the objects to be equal.
        """

        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        pass
        if self.currency == other.currency:
            new_amount = self.amount + other.amount
            currency = self.currency 
            sum = Money(new_amount.currency)
        return sum
            else
        return raiseDifferentCurrencyError 

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency == other.currency:
            new_amount = self.amount - other.amount
            currency = self.currency
            difference = Money(new_amount.currency)
        return difference
            else
        return raiseDifferentCurrencyError
        pass

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        pass
            new_amount = self.amount * other.amount
            currency = self.currency 
            product = Money(new_amount.currency)
        return product

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        pass
            new_amount = self.amount / other.amount
            currency = self.currency 
            quotient = Money(new_amount.currency)
        return quotient