from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14 Pro", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S23 Ultra", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 24 smash bros", "+79345678901"))
catalog.append(Smartphone("Huawei", "P6024 Pro", "+79456789012"))
catalog.append(Smartphone("Google", "Pixel 73", "+79567890123"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")