def apply_discount(price, discount):
    if not isinstance(price, (float,int)):    
        return 'The price should be a number'
    if not isinstance(discount, (float,int)):    
        return 'The discount should be a number'
    if price <= 0:
        return 'The price should be greater than 0'
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    else:
        discount_applied = price * (discount / 100)
        final_price = price - discount_applied
        return final_price
print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(74.5, 20.0))