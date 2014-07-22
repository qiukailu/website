#!/bin/bash -ex
python test_stock_quote.py > out
sudo mv out /var/www/html/index.html
