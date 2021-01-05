# Step 0: Starting ledger

We'll start with a basic ledger that has four accounts:

1. Assets:PintoBank:Checking
2. Liabilities:PintoBank:CreditCard
3. Income:AdzukiDotCom:Salary
4. Expenses:Food:Restaurant

Checking is where money is held, CreditCard is where money is owed, Salary
tracks how money is received and Restaurant is the sole way (for now) that 
money is spent. This is a minimal set of accounts that spans all the account
types. Future steps will add more accounts.

To get the ledger started, there's a `balance` statement with
the initial account balance. The `pad` statement tells Beancount it's
okay that the amount given by the balance doesn't match the amount in the
account, and to attribute the difference to `Equity:Opening-Balances`.
Without the `pad` statement `bean-check ledger.bean` will fail.
https://beancount.github.io/docs/getting_started_with_beancount.html
and https://beancount.github.io/docs/beancount_language_syntax.html#pad 
say more about how this works.

[ledger.bean](ledger.bean) has the full setup, repeated here:

```
2020-12-01 open Assets:PintoBank:Checking
2020-12-01 open Liabilities:PintoBank:CreditCard
2020-12-01 open Income:AdzukiDotCom:Salary
2020-12-01 open Expenses:Food:Restaurant

; Set up initial balances
2020-12-01 pad Assets:PintoBank:Checking Equity:Opening-Balances
2020-12-01 balance Assets:PintoBank:Checking    1000 USD
```
