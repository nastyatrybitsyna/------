def remove_duplicates(l: list[int]) -> list[int]:
    return sorted(set(l))

if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2, 3, 3, 3, 5, 5, 6]))  
