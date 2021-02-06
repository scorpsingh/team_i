''' a function to claculate rsi oversold and overbouht condtions'''
def my_rsi():
    cmp =[14500.00,14200.00,14255.00,14236.00,14588.00,14692.00,14523.00]
    np_array_close = np.array(cmp)
    myrsi = ta.RSI(np_array_close, timeperiod =2)
    print(myrsi)
    

    conditions = []
    for i in np.around(myrsi,2):
        if i > 80:
            conditions.append("overbought")
        elif i<20:
            conditions.append("oversold")
        else:
            conditions.append("none")
        
        
    print(conditions)
    print("current condtion is:"  ,conditions[-1])
my_rsi()   