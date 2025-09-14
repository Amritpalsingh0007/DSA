char_arr = "azyxyyzaaaa"
char_to_check_count = ["a", "b", "y", "z"]

#I know there can be 26 unique character in char_arr
hash_list = [0] * 26

for i in char_arr:
    hash_list[ord(i)-97] += 1

print("Char : occurence")
for i in char_to_check_count:
    print(f"{i} : {hash_list[ord(i)-97]}")