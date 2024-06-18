def remove_duplicates_allow_two(l: list[int]) -> list[int]:
    from collections import Counter
    count = Counter(l)
    result = []
    for num in l:
        if count[num] > 2:
            count[num] = 2
        if result.count(num) < 2:
            result.append(num)
    return result

if __name__ == "__main__":
    print(remove_duplicates_allow_two([1, 1, 2, 3, 3, 3, 5, 5, 6]))  
    print(remove_duplicates_allow_two([0, 0, 0, 0, 0, 0, 0, 0, 1])) 
    print(remove_duplicates_allow_two([1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 7]))
    
