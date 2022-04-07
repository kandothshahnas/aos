import datetime
from faker import Faker
fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_username = f'{fake.user_name()}{fake.pyint(111,999)}'[:15]
aos_password = fake.password()[:12]
aos_email = fake.email()
first_name = fake.first_name()
last_name = fake.last_name()
phone = fake.phone_number()
city = fake.city()
province =fake.province()[:10]
address = fake.address().replace("\n", "")[:50]
postal_code = fake.postcode()
full_name = f'{first_name} {last_name}'











