import stripe
stripe.api_key = 'sk_test_gC3XXUojw3qTRewhzCK3SlV6'


def create_customer():
    stripe.Customer.create()


if __name__ == "__main__":
    create_customer()