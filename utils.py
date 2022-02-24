from converter import currency_rates
import sys

word = sys.argv[1]
print(currency_rates(word))