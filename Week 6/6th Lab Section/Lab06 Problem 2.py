past_tense_words = ["use", "rain", "open","admire", "learn", "switch", "advise", "cook", "accept", "add", "like", "move", "raise", "share"]
leng = len(past_tense_words)
for i in range(leng):
    if (past_tense_words[i].endswith("e")):
        past_tense_words[i] = past_tense_words[i] + "d"
    else:
        past_tense_words[i] = past_tense_words[i] + "ed"
print(past_tense_words)
