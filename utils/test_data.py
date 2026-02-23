from faker import Faker

fake = Faker("en_US")  # you can change locale if needed

def generate_checkout_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.street_address(),
        "state": fake.state(),
        "postal": fake.postcode()
    }