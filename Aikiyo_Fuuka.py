table = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so", "ta", "chi", "tsu", "te", "to", "na", "ni",
         "nu", "ne", "no", "ha", "hi", "fu", "he", "ho", "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "wo", "n"]

print("The first threee characters in the table are:")
print(table[:3])

print("Three characters from the middle of the table are:")
print(table[18:21])

print("The last three characters in the table are:")
print(table[-3:])

other_table = table[:]
other_table.append("ga")

for i in table:
    print(i)

for i in other_table:
    print(i)
