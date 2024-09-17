# Vraag voor input text
tekst = input("Geef een tekst:").lower()

vowels = ['a', 'o', 'e', 'i', 'u', 'y']

# Count the vowels
total_count = 0
for v in vowels:
    count = tekst.count(v)
    # total_count = total_count + count # 
    total_count += count
    print(f"De klinker {v} komt {count} keer voor")

print(f"De tekst heeft {len(tekst)} karakters.")
print(f"Er komen in totaal {total_count} klinkers voor in de tekst")