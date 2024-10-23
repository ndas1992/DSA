# Find smallest letter greater than target
#Asked in companies:JP Morgan, TCS, Wells fargo, Gameskraft

def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    # Implement the function logic

    start = 0
    end = len(letters)-1
    print(letters)
    while start<=end:
        mid = (start+end)//2
        print(f'start: {start}, end: {end}, mid: {mid}')
        if letters[mid]>target:
            end = mid - 1
        elif letters[mid]<=target:
            start = mid + 1
        print(f'start: {start}, end: {end}, mid: {mid}')
        print(letters[start:])
        print('-----------'*7)
    if len(letters[start:])>0:
        res = letters[start:][0]
    else:
        res = letters[0]
    print(res)
    return res



letters = ['c', 'f', 'j']
target = 'k'
next_greatest_letter(letters, target)