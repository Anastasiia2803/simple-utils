def mean(values):
    return sum(values) / len(values)

def median(values):
    s = sorted(values)
    n = len(s)
    mid = n // 2
    return (s[mid] if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2)

if __name__ == "__main__":
    nums = [1, 2, 3, 10, 100]
    print("Mean:", mean(nums))
    print("Median:", median(nums))
