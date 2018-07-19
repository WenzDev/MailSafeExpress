import stripe

stripe.api_key = "sk_test_gC3XXUojw3qTRewhzCK3SlV6"

stripe.Product.create(
    name='Hazardous',
    type='good',

)
