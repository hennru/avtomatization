from mailing import Mailing
from address import Address

from_addr = Address(
    index="123456",
    city="Москва",
    street="Кутузовский проспект",
    house="34",
    apartment="11"
)

to_addr = Address(
    index="654321",
    city="Тюмень",
    street="Ямская",
    house="57",
    apartment="23"
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=1000,
    track="RF123444789"
)

print(f"Отправление {mailing.track} "
      f"из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, "
      f"{mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, "
      f"{mailing.to_address.city}, "
      f"{mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")