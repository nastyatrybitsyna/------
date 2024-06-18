def remove_duplicates_wrong(l: list[int]) -> list[int]:
    d = {}
    result = []
    for v in l:
        if v in d:
            if d[v] < 2:
                d[v] += 1
                result.append(v)
        else:
            d[v] = 1
            result.append(v)
    return result

if __name__ == "__main__":
    print(remove_duplicates_wrong([1, 1, 2, 3, 3, 3, 5, 5, 6])) 
