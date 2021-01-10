# Step 1: First importer, using transactions from a CSV file

This step adds an import script called [`import.py`](import.py) that will
convert transactions downloaded as a CSV file
[`Downloads/statement.csv`](Downloads/statement.csv)
into records that can be added to [`ledger-before.bean`](ledger-before.bean).
`import.py` is the idiomatic name for script in the Beancount community.

The expected workflow for importing transactions is:

1. TODO: bank, view transactions, download CSV,
2. TODO: discuss how future steps simplify by importing from a PDF statement

TODO: Discuss how `import.py` is structured internally.

To use the script, first run:

```console
$ ./import.py --downloads Downloads identify
**** beancount-basics/1-First-importer/Downloads/statement.csv
Importer:    __main__.CheckingImporter
Account:     Assets:PintoBank:Checking
```

Then run:

```console
$ ./import.py --downloads Downloads extract -e ledger-before.bean > update.bean
$ cat update.bean
**** beancount-basics/1-First-importer/Downloads/statement.csv

2020-12-01 * "Payroll ADZUKI.COM"
  Assets:PintoBank:Checking  2500 USD

2020-12-01 * "Monthly rent"
  Assets:PintoBank:Checking  -2000 USD

2020-12-15 * "Payroll ADZUKI.COM"
  Assets:PintoBank:Checking  2500 USD

```

TODO: Discuss manually matching each transaction with a second account.
