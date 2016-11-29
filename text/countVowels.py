if __name__ == "__main__":
    letters = str(raw_input("Count vowels in <input>: "))
    vowels = [l for l in letters if l in "aeiou"]
    print ''
    print "Number of vowels:", len(vowels)
    counts = {k: 0 for k in "aeiou"}
    for v in vowels:
        counts[v] = counts[v] + 1
    print "Vowel counts:", counts
    print ''
