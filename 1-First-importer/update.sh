#!/bin/sh

# This script updates ledger-after.bean using ledger-before.bean. Run it after
# changing the before file or import.py
#
# TODO: Better automate this and add unit tests to ensure ledger-after.bean is
# up-to-date.

(cat ledger-before.bean;
 ./import.py --downloads Downloads extract -e ledger-before.bean) > ledger-after.bean

