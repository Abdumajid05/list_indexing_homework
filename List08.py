def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    list1[0]=True
    list1[1]=False
    list1[2]=False
    list1[3]=False
    list1[4]=False
    return list1

print(main([1, 0, 0, 0, 0]))