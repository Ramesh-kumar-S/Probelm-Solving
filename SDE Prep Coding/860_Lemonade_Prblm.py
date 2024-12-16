def lemonade():
    AmountInHand=0
    bills = [5,5,5,10,20]
    for bill in bills:
        if bill == 5:
            # AmountInHand+=bill
            continue
        else:
            BalenceAmount = bill - 5
            if BalenceAmount >= AmountInHand:
                return False
            else:
                AmountInHand += 5
    return True


print(lemonade())
