# -*- coding:utf-8 -*-
import random


class Account(object):

    num_accounts = 0
    
    #　限制实例属性名称的访问
    __slots__ = ('name', 'balance')

    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    def deposit(self, amt):     # 存款
        self.balance = self.balance + amt

    def withdraw(self, amt):    # 取款
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance


class EvilAccount(Account):

    def __init__(self, name, balance, evilfactor):
        Account.__init__(self, name, balance)
        self.evilfactor = evilfactor

    def inquiry(self):
        if random.randint(0,4) == 1:
            return self.balance * self.evilfactor
        else:
            return self.balance


class MoreEvilAccount(EvilAccount):

    def deposit(self, amount):
        self.withdraw(5.00)  # 减去便利费
        super(MoreEvilAccount, self).deposit(amount)


# 多重继承
class DepositCharge(object):
    fee = 5.00

    def deposit_fee(self):  # 存款手续费
        self.withdraw(DepositCharge.fee)


class WithdrawCharge(object):
    fee = 2.50

    def withdraw_fee(self): # 取款手续费
        self.withdraw(WithdrawCharge.fee)


class MostEvilAccount(EvilAccount, DepositCharge, WithdrawCharge):

    def deposit(self,amt):   # 原文有错误会造成循环引用的问题!
        self.deposit_fee()
        super(MostEvilAccount,self).deposit(amt)

    def withdraw(self,amt):
        self.withdraw_fee()
        super(MostEvilAccount,self).withdraw(amt)
