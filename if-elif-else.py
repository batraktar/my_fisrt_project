n = input("Hello, my name is Max. And you?" + "\n")
print("Hello, " + n)
a = int(input("How old are you?" + "\n"))
if a <= 10:
    print("Ooo, " + n + ", are you  youth")
elif a >= 15 and a <= 25:
    print("Ooo, " + n + ", are you  young")
elif a >= 26 and a <= 54:
    print("Ooo, " + n + ", are you  adult")
else:
    print("Ooo, " + n + ", are you  an eldery person")