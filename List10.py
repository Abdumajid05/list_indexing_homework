def main(list):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    if list[0]>list[-1]:
        return list[0]
    if list[0]<list[-1]:
        return list[-1]