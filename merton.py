from decimal import Decimal
print ("             Merton for European Options on Stocks with Dividends")
corp = input("Call, Put, Vol, Parity, or Define? ")
if corp == "Call":
    underpx = input("Underlying Price = ")
    xpx = input("Strike Price = ")
    intrt = input("Interest Rate = ")
    dte = input("Days to Expiration = ")
    div = input("Annual Dividends = ")
    #vol = input("Volatility = ")
    cpx = input("Call Price = ")
    #ppx = input("Put Price = ")
    import mibian
    c=mibian.Me([underpx, xpx, intrt, div, dte], callPrice=cpx)
    #print ("Call Price ",c.callPrice)
    print ("Put Price ", c.putPrice)
    print ("Call Delta ", c.callDelta)
    print ("Put Delta ", c.putDelta)
    print ("Call Theta ", c.callTheta)
    print ("Put Theta ", c.putTheta)
    print ("Call Rho ", c.callRho)
    print ("Put Rho ", c.putRho)
    print ("Vega ", c.vega)
    print ("Gamma ", c.gamma)
    print ("Implied Vol ", c.impliedVolatility)
elif corp == "Put":
    underpx = input("Underlying Price = ")
    xpx = input("Strike Price = ")
    intrt = input("Interest Rate = ")
    dte = input("Days to Expiration = ")
    div = input("Annual Dividends = ")
    #vol = input("Volatility = ")
    #cpx = input("Call Price = ")
    ppx = input("Put Price = ")
    import mibian
    c=mibian.Me([underpx, xpx, intrt, div, dte], putPrice=ppx)
    print ("Call Price ",c.callPrice)
    #print ("Put Price ", c.putPrice)
    print ("Call Delta ", c.callDelta)
    print ("Put Delta ", c.putDelta)
    print ("Call Theta ", c.callTheta)
    print ("Put Theta ", c.putTheta)
    print ("Call Rho ", c.callRho)
    print ("Put Rho ", c.putRho)
    print ("Vega ", c.vega)
    print ("Gamma ", c.gamma)
    print ("Implied Vol ", c.impliedVolatility)
elif corp == "Vol":
    underpx = input("Underlying Price = ")
    xpx = input("Strike Price = ")
    intrt = input("Interest Rate = ")
    dte = input("Days to Expiration = ")
    div = input("Annual Dividends = ")
    vol = input("Volatility = ")
    #cpx = input("Call Price = ")
    #ppx = input("Put Price = ")
    import mibian
    c=mibian.Me([underpx, xpx, intrt, div, dte], volatility=vol)
    print ("Call Price ",c.callPrice)
    print ("Put Price ", c.putPrice)
    print ("Call Delta ", c.callDelta)
    print ("Put Delta ", c.putDelta)
    print ("Call Theta ", c.callTheta)
    print ("Put Theta ", c.putTheta)
    print ("Call Rho ", c.callRho)
    print ("Put Rho ", c.putRho)
    print ("Vega ", c.vega)
    print ("Gamma ", c.gamma)

elif corp == "Define":
    print ("What variable would you like to define:")
    grk = input("   Delta, Theta, Rho, Vega, or Gamma? ")
    if grk == "Delta":
        print ("""
        Delta measures the degree to which an option is exposed to
        shifts in the price of the underlying asset.
        Values range from 1.0 to –1.0
        """)
    elif grk == "Theta":
        print ("""
        Theta is a measure of the rate of decline in the value
        of an option due to the passage of time.
        It can also be referred to as the time decay on the value of an option.
        If everything is held constant, the option loses value as time moves
        closer to the maturity of the option.
        """)
    elif grk == "Rho":
        print ("""
        Rho measures the sensitivity of an option or options
        portfolio to a change in interest rate.
        """)
    elif grk == "Vega":
        print ("""
        The vega of an option expresses the change in the price of the
        option for every 1% change in underlying volatility.
        """)
    elif grk == "Gamma":
        print ("""
        Gamma is the rate of change in an option's delta
        per 1-point move in the underlying asset's price.
        """)
    else:
        print("""
        Please check your spelling
        """)
elif corp == "Parity":
        underpx = input("Underlying Price = ")
        xpx = input("Strike Price = ")
        intrt = input("Interest Rate = ")
        dte = input("Days to Expiration = ")
        div = input("Annual Dividends = ")
        #vol = input("Volatility = ")
        cpx = input("Call Price = ")
        ppx = input("Put Price = ")
    print("Put-Call Parity ", c.putCallParity)
else:
    print("""
    Please check your spelling
    """)
