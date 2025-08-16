from mailing import Mailing
from address import Address

from_address = Address(101000, "Москва", "Мира", 10, 45)
to_address = Address(188100, "Санкт-Петербург", "Счастья", 20, 50)

mailing = Mailing(from_address, to_address, 500, "AB12345D")

print(to_address)
print(mailing)
