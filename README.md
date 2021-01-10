# beancount-basics

This repository is an introduction to using
[Beancount](https://github.com/beancount/beancount), with practical
examples and simple code written from first principles. I wrote this to help
others get started with Beancount's approach to double entry accounting. I
personally found it was difficult to get started because I was unsure how
much code, and what kind of code, I needed to write on my own. Once I got
started I quickly saw how the approach comes together. Beancount is now
the quick, powerful and assuring method I used to track all of my finances.

The repository is organized into a number of steps that build on
one another, each with their own documentation and their own
self-contained ledger and code.

* **[0-Starting-ledger/](0-Starting-ledger/README.md)**: A basic ledger
  that acts as the foundation. Code is added in the next step.
* **[1-First-importer/](1-First-importer/README.md)**: A basic importer
  to demonstrate how to add transactions to the ledger, using a simple CSV
  file with transactions downloaded from the bank.
* **[2-Multiple-importers/](2-Multiple-importers/README.md)**: An
  additional importer, with refactoring to show how to compose different input
  handling with reusable common code.
* **[3-Automatically-match-to-other-account/](3-Automatically-match-to-other-account/README.md)**:
  Logic to automatically match each transaction to a second account, which
  is crucial to use double-entry accounting with minimal effort.
