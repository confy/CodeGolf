days = ["A Partridge in a Pear Tree.\n", "Two Turtle Doves, and", "Three French Hens,",
        "Four Calling Birds,", "Five Gold Rings,", "Six Geese-a-Laying,", "Seven Swans-a-Swimming,",
        "Eight Maids-a-Milking,", "Nine Ladies Dancing,", "Ten Lords-a-Leaping,", "Eleven Pipers Piping,",
        "Twelve Drummers Drumming,"]
daysnum = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth",
           "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
for day in range(12):
    print(f"On the {daysnum[day]} day of Christmas\nMy true love sent to me")
    for i in range(day, -1, -1):
        print(days[i])
