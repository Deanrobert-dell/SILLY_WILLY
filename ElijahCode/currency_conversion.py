#EHCP2 currency conversion
from currex import *

money = Currency("USD", 100)

money.to("EUR")

print(money)