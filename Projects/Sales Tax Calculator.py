while True:
    cost_of_item = input("What is the cost of your item?")
    state_rate = input("What is your state's tax rate?")
    state_rate = int(state_rate)/100
    cost_applied_tax = float(cost_of_item) * state_rate
    final_price = float(cost_of_item) + float(cost_applied_tax)
    print(f"{final_price}")
