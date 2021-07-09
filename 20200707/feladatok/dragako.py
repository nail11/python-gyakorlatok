# Betűjelek jelölik az egyes kő típusokat.
# Minden karakter egy kő fajtának felel meg. A karakterek kis és nagy betű érzékenyek, Tehát az "a" és az "A" különböző
# típusokat jelölnek.
# A feladat az, hogy megállapítsuk a kövek közül mennyi a drágakő?
#
# Example 1:
# Input: jewels = "aA",
# Output: 3
#
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

jewels1 = "aA"
stones1 = "aAAbbbb"

jewels2 = "z"
stones2 = "ZZ"

jewels3 = "zaBc"
stones3 = "ZZzzAaBBCcza"


def count_jewel(jewels, stones):

    db = 0

    for j in jewels:
        for s in stones:
            if j == s:
                db += 1
    print(db)

count_jewel(jewels3, stones3)
