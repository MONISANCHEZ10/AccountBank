# -*- coding: utf-8 -*-

from ZODB import (DB, FileStorage)
from persistent import Persistent
import transaction
import argparse

class Accounts(Persistent):
    def __init__(self):
        self.clientName = ""
        self.clientId = ""
	self.address = ""
	self.phone = ""
	self.accountId = ""
	

class Bank:
    def __init__(self):
        self.store = FileStorage.FileStorage("data.fs")
        self.database = DB(self.store)
        self.connection = self.database.open()
        self.root = self.connection.root()
        if not 'Accounts' in self.root:
            self.root['Accounts'] = []
        self.accounts = self.root['Accounts']

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        transaction.get()
        transaction.abort()
        self.connection.close()
        self.database.close()
        self.store.close()

    def add(self, clientName, clientId, address, phone, accountId):
        if clientName != "":
            newAccount = Accounts()
            newAccount.clientName = clientName
            newAccount.clientId = clientId
	    newAccount.address = address
            newAccount.phone = phone
	    newAccount.accountId = accountId
            self.accounts.append(newAccount)
            self.root['Accounts'] = self.accounts
            transaction.commit()
            print("New client added..")
        else:
            print("Error add 5 arguments: client name, id, address, phone.....")

    def list(self):
        if len(self.accounts) > 0:
            print("Bank accounts.......")
            for account in self.accounts:
                print("%s\t%s\t%s" %(account.clientName,account.accountId, account.balance))
        else:
            print("No accounts in this bank.")

    def delete(self, accountId):
        for i in range(len(self.accounts)):
            deleted = False
            if self.accounts[i].accountId == accountId:
                del(self.accounts[i])
                deleted = True
		
            if deleted:
                self.root['Accounts'] = self.accounts
                transaction.commit()
                print("Account deleted..")
            else:
                print("There is no Account Id '%s'.." % accountId)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-add', '--add', nargs=5, help="add a account to registry")
    parser.add_argument('-delete', '--delete', nargs=1, help="delete a account from registry by account id ")
    args = parser.parse_args()
    accounts = Bank()
    if args.add:
        accounts.add(args.add[0],args.add[1], args.add[2], args.add[3], args.add[4])
    elif args.delete:
        accounts.delete(args.delete[0])
    else:
        accounts.list()
