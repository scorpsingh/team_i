'''W03D17_assignment_q4_ function for the two sma crossover '''

import talib as ta
import numpy as np

nifty_cp =  [14500.00,14552.00,14506.00,13985.00,14502.00,14312.00,13900.00,13800.00,13850.00,14000.00,14500.00,14552.00,14506.00,13985.00,14502.00,14312.00,13900.00,13800.00,13850.00,14000.00,14500.00,14552.00,14506.00,13985.00,14502.00,14312.00,13900.00,13800.00,13850.00,14000.00]
cmp = np.array(nifty_cp)

#tf = "the time period of fast sma
#ts = "the time period of slow sma

def smaco(tf,ts):
    fast = ta.SMA(cmp,tf)
    slow = ta.SMA(cmp,ts)
    print(fast)
    print(slow)
    fastlist = list(fast)
    slowlist = list(slow)
    condition = []
    previousState = 0
    for i,j in zip(fastlist,slowlist):
        if i>j and previousState != "1":
            k="1"
            previousState = "1"
        elif i<j and previousState != "-1":
            k="-1"
            previousState = "-1"
        else:
            k="0"
        condition.append(k)
    print(condition)
    print("current condtion is:", condition[-1])

smaco(3,5)
