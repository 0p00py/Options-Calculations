from decimal import Decimal
import mibian
from iexfinance import Stock
#import mibianLib
import matplotlib.pyplot as plt
#import plotly.plotly as plt
#import plotly.graph_objs as go
import os
clear = lambda: os.system('cls')
clear()
print ("""             Merton Pricing for European Options for Stocks with Dividends


                """)
corp = input("Call, Put, Vol, Parity, Define, or Exit (Ctrl-C)? ")
print("")
ticker = input("Ticker = ")
utick = ticker.upper()
tickpx = Stock(utick)
underpx = tickpx.get_price()
print ("The current price of",utick, "is...", round(underpx, 2))
print("")
#while corp not in ["Exit", "exit"]:
if corp in ["Call", "call"]:
    print("")
    print("Call Option Analytics")
    xpx = input("Strike Price = ")
    xpx_float = float(xpx)
    if xpx_float <= underpx:
         print("This option is in the money and should be exercised.")
    elif xpx_float > underpx:
        intrt = input("Interest Rate = ")
        adiv = input("Annual Dividend = ")
        dte = input("Days to Expiration = ")
        #vol = input("Volatility = ")
        cpx = input("Call Price = ")
        #ppx = input("Put Price = ")
        #import mibian
        c=mibian.Me([underpx, xpx, intrt, adiv, dte], callPrice = cpx)
        print ("")
        print ("Implied Vol ", round(c.impliedVolatility,4))
        ivol = c.impliedVolatility
        c=mibian.Me([underpx, xpx, intrt, adiv, dte], volatility = ivol)
        #print ("Call Price ",c.callPrice)
        print("")
        print ("Put Price ", round(c.putPrice, 4))
        print ("Call Delta ", round(c.callDelta, 4))
        print ("Put Delta ", round(c.putDelta, 4))
        print ("Call Theta ", round(c.callTheta, 4))
        print ("Put Theta ", round(c.putTheta, 4))
        print ("Call Rho ", round(c.callRho, 4))
        print ("Put Rho ", round(c.putRho, 4))
        print ("Vega ", round(c.vega, 4))
        print ("Gamma ", round(c.gamma, 4))
        print ("")
        graph = input("Would you like to graph the ? (Y/N)")
        if graph in ["y", "Y", "yes", "Yes"]:
            cpx = cpx * -1

elif corp in ["Put", "put"]:
    print("")
    print("Put Option Analytics")
    #underpx = input("Underlying Price = ")
    xpx = input("Strike Price = ")
    xpx_float = float(xpx)
    if xpx_float >= underpx:
        print("This option is in the money and should be exercised.")
    elif xpx_float < underpx:
        intrt = input("Interest Rate = ")
        adiv = input("Annual Dividend = ")
        dte = input("Days to Expiration = ")
        #vol = input("Volatility = ")
        #cpx = input("Call Price = ")
        ppx = input("Put Price = ")
        #import mibian
        c=mibian.Me([underpx, xpx, intrt, adiv, dte], putPrice=ppx)
        print("")
        print ("Implied Vol ", c.impliedVolatility)
        ivol = c.impliedVolatility
        c=mibian.Me([underpx, xpx, intrt, adiv, dte], volatility = ivol)
        print("")
        print ("Call Price ", round(c.callPrice, 4))
        #print ("Put Price ", round(c.putPrice, 4))
        print ("Call Delta ", round(c.callDelta, 4))
        print ("Put Delta ", round(c.putDelta, 4))
        print ("Call Theta ", round(c.callTheta, 4))
        print ("Put Theta ", round(c.putTheta, 4))
        print ("Call Rho ", round(c.callRho, 4))
        print ("Put Rho ", round(c.putRho, 4))
        print ("Vega ", round(c.vega, 4))
        print ("Gamma ", round(c.gamma, 4))
elif corp in ["Vol", "vol"]:
    print("")
    print("Option Analytics based on Vol")
    #underpx = input("Underlying Price = ")
    xpx = input("Strike Price = ")
    intrt = input("Interest Rate = ")
    adiv = input("Annual Dividend = ")
    dte = input("Days to Expiration = ")
    vol = input("Volatility = ")
    #cpx = input("Call Price = ")
    #ppx = input("Put Price = ")
    #import mibian
    c=mibian.Me([underpx, xpx, intrt, adiv, dte], volatility=vol)
    print("")
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

elif corp in ["Define", "define"]:
    print("")
    #grk = "empty"
    #while grk not in ["Exit", "exit"]:
    print ("What variable would you like to define:")
    grk = input("   Delta, Theta, Rho, Vega, Gamma, or Exit? ")
    if grk in ["Delta", "delta"]:
        print ("""
        Delta Measures the degree to which an option is exposed to
        shifts in the price of the underlying asset.
        Values range from 1.0 to –1.0
        """)
        #grk = "Exit"
    elif grk in ["Theta", "theta"]:
        print ("""
        Theta is a Measure of the rate of decline in the value
        of an option due to the passage of time.
        It can also be referred to as the time decay on the value of an option.
        If everything is held constant, the option loses value as time moves
        closer to the maturity of the option.
        """)
        #grk = "Exit"
    elif grk in ["Rho", "rho"]:
        print ("""
        Rho Measures the sensitivity of an option or options
        portfolio to a change in interest rate.
        """)
        grk = "Exit"
    elif grk in ["Vega", "vega"]:
        print ("""
        The vega of an option expresses the change in the price of the
        option for every 1% change in underlying volatility.
        """)
        #grk = "Exit"
    elif grk in ["Gamma", "gamma"]:
        print ("""
        Gamma is the rate of change in an option's delta
        per 1-point move in the underlying asset's price.
        """)
        #grk = "Exit"
#else:
    #grk = "Exit"


elif corp in ["Parity", "parity"]:
    #underpx = input("Underlying Price = ")
    xpx = input("Strike Price = ")
    intrt = input("Interest Rate = ")
    adiv = input("Annual Dividend = ")
    dte = input("Days to Expiration = ")
    #vol = input("Volatility = ")
    cpx = input("Call Price = ")
    ppx = input("Put Price = ")
    #import mibian
    c=mibian.Me([underpx, xpx, intrt, adiv, dte], callPrice=cpx, putPrice=ppx)

    print("Put-Call Parity ", c.putCallParity)
#elif corp in ["Exit", "exit"]:
    #print("""
    #Press Ctrl-
    #""")
