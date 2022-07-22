word=["but", "do", "not", "to", "has", "have", "had", "then", "who", "when", "is", "why","what", "how", "while", "hence", "I", "you", "he", "she", "it", "a", "for", "by","an", "am", "the", "so", "and", "my", "are", "in", "at", "on"]
user_input = (input("Enter sentence")).split()
for i in user_input:
    if i != "I":
        a = i.lower()
        if a not in word:
            print(i[0].upper(), end="")