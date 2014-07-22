# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 09:28:30 2014

@author: qlu
"""

import ystockquote as ysq
from tabulate import tabulate
import HTML
import datetime

def get_market_value(stock_symbol, stock_quantity):
    stock_price = ysq.get_last_trade_price(stock_symbol)
#    stock_quantity = 232.430
    stock_value = float(stock_price) * stock_quantity
    return stock_value
    
cur_a = get_market_value('FCNTX', 89.840)
cur_b = get_market_value('FNMIX', 232.430)

cur_tot = cur_a + cur_b

tar_a = cur_tot * 0.8
tar_b = cur_tot * 0.2

diff_a = cur_a - tar_a
diff_b = cur_b - tar_b

table = [['FCNTX', cur_a, tar_a, diff_a], 
         ['FNMIX', cur_b, tar_b, diff_b],
         ['TOTAL', cur_tot, cur_tot, 0.0]]

#print tabulate(table)

print "<html>"

# adding head
print "<head>"
print "<title> The Stock Quote </title>"
print "</head>"

# google analytics code
print "<script>"
print "  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){"
print "  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),"
print "  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)"
print "  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');"
print ""
print "  ga('create', 'UA-53064732-1', 'auto');"
print "  ga('send', 'pageview');"
print ""
print "</script>"

# generating table code
htmlcode = HTML.table(table)

# output table code
print htmlcode

# get current date & time
i = datetime.datetime.now()

# output date & time
print ("Last update: %s" % i)

print "</html>"
