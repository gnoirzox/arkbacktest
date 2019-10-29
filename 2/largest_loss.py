from typing import List, Optional


def largestLoss(prices_list: List[float]) -> Optional[int]:
    if len(prices_list) % 2 != 0:
        raise Exception('The length of the submitted list needs to be even ' \
            'in order to check both the related bought and sold prices')

    if len(prices_list) == 0:
        raise Exception('The submitted list is empty')

    maximum_loss = None

    for i in range(1, len(prices_list), 2):
        if prices_list[i] < 0 or prices_list[i - 1] < 0:
            raise Exception('The prices cannot be negative')

        loss = prices_list[i] - prices_list[i - 1]

        if maximun_loss is None or loss > maximum_loss:
            maximum_loss = loss

    return maximum_loss

