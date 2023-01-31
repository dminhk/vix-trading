from datetime import timedelta
from AlgorithmImports import *

class VixBasedInvesting(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetEndDate(2023, 1, 1)  # Set Start Date
        self.SetCash(10000)  # Set Strategy Cash
        self.spy = self.AddEquity("SPY", Resolution.Daily)
        self.vix = self.AddData(CBOE, "VIX").Symbol
        self.invest = True
        #--------------------------------------------------------------
        self.VIXbuy = 20
        self.VIXsell = 30
        #--------------------------------------------------------------


    def OnData(self,data):
        if not self.Portfolio.Invested and self.Securities[self.vix].Price > self.VIXbuy:
            self.SetHoldings("SPY", 1)

        if self.Securities[self.vix].Price < self.VIXsell:
            self.Liquidate("SPY")
            self.invest = False
