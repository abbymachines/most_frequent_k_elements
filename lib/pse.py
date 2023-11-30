# clarifying questions
# 1: What if there is a tie for most frequent at the k boundary?
#   We will return a correct answer, but no guarantees about which one
# 2: What if k is invalid?
#   We will assume that the code will end up raising an error of some kind
# 3: What if there are negative nums?
#   It should just work, like with positive numbers.

# logical steps
# 1. Build a frequency map of list elements and their count.
# 2. Get the unique elements of the list into a new list, from map keys
# 3. Sort the unique values based on their counts
# 4. Return the first k values

def make_counts(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        # count = counts.get(num, 0)
        # counts[num] = count + 1
    return counts

def most_frequent_k_elements(arr, k):
    counts = make_counts(arr)
    uniq_nums = list(counts.keys())
    uniq_nums.sort(key=lambda num: counts[num], reverse=True)
    # uniq_nums.sort(key=counts.get, reverse=True)
    return uniq_nums[:k]
