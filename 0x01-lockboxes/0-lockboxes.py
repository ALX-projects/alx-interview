def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: A list of lists representing locked boxes.
    :return: True is all boxes can be opened, else False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    unlocked = [0]  # The first box is already unlocked

    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)

    return len(unlocked) == len(boxes)
