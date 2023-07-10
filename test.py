from pyotp import TOTP

totp = TOTP("t44h6rcqywooo4wnttvdxlqp6waqvebn")
token = totp.now()

print(token)