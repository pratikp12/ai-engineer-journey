class BankAccount:
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner
        self.__balance = initial_balance  # private attribute

    @property
    def balance(self) -> float:
        """Getter: return the private balance."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        except ValueError as e:
            print(f"Deposit failed: {e}")

    def _update_balance(self, amount: float) -> None:
        """Protected method to update balance internally."""
        self.__balance += amount

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"Holder: {self.owner} | Balance: {self.__balance:,.2f}"

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"BankAccount(owner={self.owner!r}, balance={self.__balance})"


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float, interest_rate: float = 0.04, min_balance: float = 5000):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def apply_interest(self) -> None:
        """Calculate and add interest to balance."""
        interest = self.balance * self.interest_rate
        self._update_balance(interest)
        print(f"Interest of {interest:.2f} applied.")

    def withdraw(self, amount: float) -> None:
        """Withdraw money while maintaining minimum balance."""
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if (self.balance - amount) < self.min_balance:
                raise ValueError(f"Denied: Must maintain minimum balance of {self.min_balance}")
            self._update_balance(-amount)
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        except ValueError as e:
            print(f"Withdrawal failed: {e}")


class CurrentAccount(BankAccount):
    def __init__(self, owner: str, balance: float, overdraft_limit: float = 500000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        """Withdraw money with overdraft facility."""
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if (self.balance + self.overdraft_limit) < amount:
                raise ValueError(f"Denied: Exceeds overdraft limit of {self.overdraft_limit}")
            self._update_balance(-amount)
            print(f"Withdrew {amount}. Current balance: {self.balance}")
        except ValueError as e:
            print(f"Withdrawal failed: {e}")


# Demo
print("--- Savings Account ---")
sa = SavingsAccount("Pratik", 10000)
sa.withdraw(6000)       # valid
sa.withdraw(-2000)      # handled internally
sa.apply_interest()
print(sa)
