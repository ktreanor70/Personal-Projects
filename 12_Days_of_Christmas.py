# 12 Days of Christmas

days = [
    "first",
    "second",
    "third",
    "forth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

gifts = [
    "A partridge in a pear tree",
    "Two turtle doves, and a",
    "Three french hens",
    "Four calling birds",
    "Five gold rings",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming",
]

for gift, day in enumerate(days):
    print(f"\nOn the {day} day of Christmas, my true love gave to me")
    print(*gifts[gift::-1], sep="\n")
