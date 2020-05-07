from django_seed import Seed
from products.models import Producttype, Product

seeder = Seed.seeder()

seeder.add_entity(Producttype, 5)
seeder.add_entity(Product, 10)

inserted_pks = seeder.execute()
