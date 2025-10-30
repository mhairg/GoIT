import random


def generate_params(min_limit: int, max_limit: int) -> (tuple[int, int, int]
                                                        | None):
    """
    Generate random numeric values as parameters to be passed to the
    get_numbers_ticket() function under the condition that quantity_num
    < (max_num - min_num).

    :param min_limit: Used-defined minimal possible number in the set.

    :param max_limit: Used-defined maximum possible number in the set.

    :return: Three numeric values.
    """

    while True:
        min_num = random.randint(min_limit, max_limit)
        max_num = random.randint(min_num, max_limit)
        quantity_num = random.randint(min_num, max_num)
        if quantity_num > (max_num - min_num):
            continue
        else:
            print(min_num, max_num, quantity_num)
            return min_num, max_num, quantity_num


def get_numbers_ticket(minimum: int, maximum: int, quantity: int) -> list[int]:
    """
    Generate an ordered list of unique numbers in a predefined range
    and of a predefined length.

    :param minimum: Number to be used as a range start value.

    :param maximum: Number to be used as a range end value.

    :param quantity: Number to be used as a list length definer.

    :return: An ordered list of randomly selected unique numbers OR an
    empty list if the range limits don't match the required values.
    """

    if minimum < 1 or maximum > 1000:
        return []
    lottery_numbers = random.sample(range(minimum, maximum), k=quantity)
    return sorted(lottery_numbers)


start, end, diapason = generate_params(1, 10)
lottery = get_numbers_ticket(start, end, diapason)
print(f'Your lottery numbers: {lottery}')
