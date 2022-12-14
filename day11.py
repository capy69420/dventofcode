def inspect_and_throw_item(item, operation, test, if_true, if_false):
    # Apply the operation to the item
    new_item = operation(item)

    # Divide the result by 3 and round down
    new_item = new_item // 3

    # Determine where to throw the item
    if new_item % test == 0:
        recipient = if_true
    else:
        recipient = if_false

    return recipient, new_item

def take_turn(monkey, recipients):
    # Inspect and throw each item
    for item in monkey["items"]:
        recipient, new_item = inspect_and_throw_item(
            item, monkey["operation"], monkey["test"], monkey["if_true"], monkey["if_false"]
        )

        # Throw the item to the recipient
        recipients[recipient]["items"].append(new_item)

    # Clear the list of items
    monkey["items"] = []

def simulate_rounds():
    # Initialize the monkeys
    monkeys = [
        {
            "name": 0,
            "items": [50, 70, 89, 75, 66, 66],
            "operation": lambda x: x * 5,
            "test": 2,
            "if_true": 2,
            "if_false": 1,
        },
        {
            "name": 1,
            "items": [85],
            "operation": lambda x: x * x,
            "test": 7,
            "if_true": 3,
            "if_false": 6,
        },
        {
            "name": 2,
            "items": [66, 51, 71, 76, 58, 55, 58, 60],
            "operation": lambda x: x + 1,
            "test": 13,
            "if_true": 1,
            "if_false": 3,
        },
        {
            "name": 3,
            "items": [79, 52, 55, 51],
            "operation": lambda x: x + 6,
            "test": 3,
            "if_true": 6,
            "if_false": 3,
        },
        {
            "name": 4,
            "items": [69, 92],
            "operation": lambda x: x * 17,
            "test": 19,
            "if_true": 7,
            "if_false": 5,
        },
        {
            "name": 5,
            "items": [71, 76, 73, 98, 67, 79, 99],
            "operation": lambda x: x + 8,
            "test": 5,
            "if_true": 0,
            "if_false": 2,
        },
        {
            "name": 6,
            "items": [82, 76, 69, 69, 57],
            "operation": lambda x: x + 7,
            "test": 11,
            "if_true": 7,
            "if_false": 4,
        }, 
        {
            "name": 7,
            "items": [65, 79, 86],
            "operation": lambda x: x + 5,
            "test": 17,
            "if_true": 5,
            "if_false": 0,
        }
    ]

    # Initialize a dictionary mapping monkey names to monkey objects
    recipients = {monkey["name"]: monkey for monkey in monkeys}

    # Simulate rounds until all monkeys have no items
    num_rounds = 0
    while any(monkey["items"] for monkey in monkeys):
        num_rounds += 1
        for monkey in monkeys:
            take_turn(monkey, recipients)
    print(num_rounds)
    return num_rounds

print('Nums of rounds:', simulate_rounds())