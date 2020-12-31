#!/usr/bin/env python3

import csv
import re
import os

from beancount.core import amount
from beancount.core import data
from beancount.core import flags
from beancount.core import number
from beancount.ingest import importer
from beancount.ingest import scripts_utils

from dateutil import parser

FILE_PATTERN = r'activity.*\.csv$'

class CreditCardImporter(importer.ImporterProtocol):
    def __init__(self, account):
        """
        account is a string account.
        """
        self.account = account

    def identify(self, f):
    #    return common.Identify(f, FILE_PATTERN, self.account_numbers, self.__get_record)
        return re.match(FILE_PATTERN, os.path.basename(f.name))

    def file_account(self, f):
        return self.account

    #def file_name(self, f):
    #    return common.TimeRangeFilename(self.extract(f))

    def extract(self, f):
        entries = []

        with open(f.name) as fio:
            # Downloads/activity_2020-12-23.csv has the header:
            #   Date,Description,Card Member,Account #,Amount
            for index, row in enumerate(csv.DictReader(fio)):
                descr = row['Description']
                member = row['Card Member']

                amt = amount.Amount(number.D(row['Amount']), 'USD')
                # TODO: Explain this
                amt = amount.mul(amt, number.D(-1))

                descr='{} - {}'.format(descr, member)
                trans_date = parser.parse(row['Date']).date()

                postings = [
                    data.Posting(self.account, amt, None, None, None, None),
                ]

                entries.append(data.Transaction(
                    meta=data.new_metadata(f.name, index),
                    date=trans_date,
                    flag=flags.FLAG_OKAY,
                    payee=None,
                    narration=descr,
                    tags=set(),
                    links=set(),
                    postings=postings,
                ))
        return entries



CONFIG = [
        CreditCardImporter('Liabilities:MyBank:CreditCard'),
    ]

# Don't add the emacs mode lines that look like
#   ;; -*- mode: beancount -*-' lines
# (I'm a vi user.)
extract.HEADER = '' 

scripts_utils.ingest(CONFIG)


