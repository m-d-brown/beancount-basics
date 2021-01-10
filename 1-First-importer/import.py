#!/usr/bin/env python3

import csv
import re
import os

from beancount.core import amount
from beancount.core import data
from beancount.core import flags
from beancount.core import number
from beancount.ingest import extract
from beancount.ingest import importer
from beancount.ingest import scripts_utils

from dateutil import parser

FILE_PATTERN = r'statement\.csv$'

class CheckingImporter(importer.ImporterProtocol):
    def __init__(self, account):
        """
        account is a string account.
        """
        self.account = account

    def identify(self, f):
        return re.match(FILE_PATTERN, os.path.basename(f.name))

    def file_account(self, f):
        return self.account

    def extract(self, f):
        entries = []

        with open(f.name) as fio:
            # Downloads/statement.csv has the header:
            #   Account Number,Transaction Date,Transaction Amount,Transaction Type,Transaction Description
            for index, row in enumerate(csv.DictReader(fio)):
                descr = row['Transaction Description']
                amt = amount.Amount(number.D(row['Transaction Amount']), 'USD')
                trans_date = parser.parse(row['Transaction Date']).date()

                postings = [
                    data.Posting(self.account, amt, None, None, None, None),
                    data.Posting('TODO:MatchMe', None, None, None, None, None),
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
        CheckingImporter('Assets:PintoBank:Checking'),
    ]

# Don't add the emacs mode lines that look like
#   ;; -*- mode: beancount -*-' lines
# (I'm a vi user.)
extract.HEADER = '' 

scripts_utils.ingest(CONFIG)


