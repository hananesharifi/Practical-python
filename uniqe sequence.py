n = int(input())
seq = input()
list1 = [int(c) for c in seq.split()]

def calculate_xor_uniqe(sequence):
    count_dict = {}
    for i in sequence:
        count_dict[i] = count_dict.get(i,0) + 1

    uniq_xor = 0
    for i in count_dict:
        if count_dict[i] == 1:
            uniq_xor ^= i

    return uniq_xor


print(calculate_xor_uniqe(list1))