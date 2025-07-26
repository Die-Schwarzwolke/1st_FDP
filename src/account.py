from __future__ import annotations

class Account:
    _next_id = 1

    def __init__(self, owner: str, balance: float = 0.0):
        self.id = Account._next_id
        Account._next_id += 1
        self.owner = owner
        self.balance = balance

    def deposit(self, amount:float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def __str__(self) -> str:
        return f"[{self.id}] {self.owner}: \{self.balance:,.0f}"
    
    def __lt__(self, other: "Account") -> bool:
        return self.balance < other.balance
    
class PremiumAccount(Account):
    def withdraw(self, amount: float) -> None:
        super().withdraw(amount)