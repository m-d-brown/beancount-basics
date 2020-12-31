# Step 1: Simple importer

This step adds an import script called [import.py](import.py) that will
convert transactions downloaded as a CSV file
[Downloads/activity_2020-12-23.csv](Downloads/activity_2020-12-23.csv)
into records that can be added to [ledger.bean](ledger.bean).

First run:

```console
$ ./import.py --downloads Downloads identify
**** /beancount-basics/1-First-importer/Downloads/activity_2020-12-23.csv
Importer:    __main__.CreditCardImporter
Account:     Liabilities:MyBank:CreditCard
```

Then run:

```console
$ ./import.py --downloads Downloads extract -e ledger.bean > update.bean
$ cat update.bean
**** /Users/mdbrown/beancount-basics/1-First-importer/Downloads/activity_2020-12-23.csv

2020-11-29 * "LOCAL GAS STATION - PAT BEAN"
  Liabilities:MyBank:CreditCard  -45.57 USD

2020-12-10 * "LOCAL GROCER - PAT BEAN"
  Liabilities:MyBank:CreditCard  -30.78 USD

2020-12-13 * "AUTOPAY PAYMENT - THANK YOU - PAT BEAN"
  Liabilities:MyBank:CreditCard  134.97 USD

2020-12-19 * "THAI DELIVERY - PAT BEAN"
  Liabilities:MyBank:CreditCard  28.97 USD

```
