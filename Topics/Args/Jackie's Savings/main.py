def final_deposit_amount(*interest, amount=1000):
    final_amount = amount
    for arg in interest:
        final_amount = final_amount * (100 + arg) / 100
    return round(final_amount, 2)
