# Step 0: Starting ledger

We'll start with a basic ledger that has five accounts:

1. `Assets:PintoBank:Checking` tracks cash, held in a bank checking account
   for the fictional "Pinto Bank".
2. `Liabilities:PintoBank:CreditCard` tracks money owed, for a credit card
   kept at the same bank.
3. `Equity:Opening-Balances` tracks value that's not recorded in your ledger.
   It makes it easier to get started because you can say you have some amount
   of money in `:Checking` today without have to say from which account it came
   from. (This is an important implication of the double-entry method. If this
   doesn't yet make sense, the
   [Beancount documentation](https://beancount.github.io/docs/the_double_entry_counting_method.html)
   on the topic is helpful.)
4. `Income:AdzukiDotCom:Salary` tracks money that is earned, from a fictional
   "Adzuki.com" company.
5. `Expenses:Food:Restaurant` tracks money that is spent, through a single
    (for now) expense category.

This is a minimal set of accounts that spans all the account
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

You can interact with this ledger, such as by checking that the ledger has no
errors with `bean-check`:

```console
$ bean-check ledger.bean
$
```

Or by running 
[Fava](https://github.com/beancount/fava) for a powerful web UI:

```console
$ fava ledger.bean
Running Fava on http://localhost:5000
```

Or by printing balances on your terminal:

```console
$ bean-report -f text ledger.bean bal
Assets:PintoBank:Checking          1000 USD
Equity:Opening-Balances           -1000 USD
Expenses:Food:Restaurant
Income:AdzukiDotCom:Salary
Liabilities:PintoBank:CreditCard
```

**For code to automate the import of transactions into the `:Checking` account
using a CSV file download from the bank, see the next step:
[1-First-importer](../1-First-importer/README.md).**
