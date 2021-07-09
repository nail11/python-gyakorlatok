# írjunk olyna Python függvényt ami megmondja, hogy hol van a tű a szénakazalban. A függvény fogadjon el egy haystack azaz szénakazal paramétert és egy needle argumentumot. Mindkét argumentum legyen szöveg. Az első tartalmazzon egy hosszú, nem üres stringet, a második egy rövidebb nem üres stringet.
#
# A függvény úgy keresi a tű-t a szánakazalban, hogy a haystack paraméterben kapott string karakterei között próbál egyezést találni a needle paraméterben kapott string karaktereire. Ha benne van a needle string a haystack stringben akkor adja vissza az első olyan indexet ahol kezdődik a tű a szénakazalban. Ha nincs benne a tű a szénakazalban akkor adjon vissza a függvény egy -1 es értéket
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1