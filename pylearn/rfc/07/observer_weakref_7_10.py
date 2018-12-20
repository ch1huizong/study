# -*- coding:UTF-8 -*-
# __del__造成循环引用问题，弱引用为解决办法

# 本质是实行监视者-被监视者间的同步
# 测试通不过?

class Account(object):

    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        self.observers = set()

    def __del__(self):          # account的引用计数-1,没有a了，但对象依然存在
        for ob in self.observers:
            ob.close() # 删除observer没运行? 
        del self.observers  # 删除对observers集合的引用，好多observer

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for ob in self.observers:
            ob.update()

    def withdraw(self, amt):
        self.balance -= amt
        self.notify()


# 会造成循环引用
class AccountObserver(object):

    def __init__(self, theaccount):
        self.theaccount = theaccount # account的引用计数+1
        theaccount.register(self)

    def __del__(self):
        self.theaccount.unregister(self)
        del self.theaccount  # 删除对account的引用,造成循环引用
    
    def update(self):
        print("Balance is %0.2f" % self.theaccount.balance)

    def close(self):
        print("Account no longer in use.")



import weakref
class AccountObserverRef(object):

    def __init__(self, theaccount):
        self.countref = weakref.ref(theaccount) # 创建弱引用,accout引用计数不变
        theaccount.register(self)

    def __del__(self):
        acc = self.countref()   # 获取帐户
        if acc: # 若账户依然存在
            acc.unregister(self)
    
    def update(self):
        print("Balance is %0.2f" % self.countref().balance)

    def close(self):
        print("Account no longer in use.")
