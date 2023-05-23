import re


def numbers(file_path):
    with open(file_path) as f:      # Öppnar filen
        count = 1       # Radräknare börjar på 1
        for lines in f:     # För varje rad i programmet ska det skrivas ut radnummer och koden på raden
            print(str(count) + '\t' + lines.rstrip('\n'))
            count += 1      # Uppdaterar räknaren för radnummer


def line_numbers(file_path, word_list):
    with open(file_path) as f:
        results = {word:[] for word in word_list}
        for num, line in enumerate(f, start=1):
            for word in word_list:
                if word in line:
                    results[word].append(num)
    return results


words = {}
line_dict = {'for', 'in', 'def', 'else'}
for line in open('kod.txt', 'r'):
    line = re.sub(r'#.*$', '', line)
    line = re.sub('[^a-zA-Z\s]', '', line)
    for key in line_dict:
        if key in line.split():
            line = line.replace(key, '')
    for c in line.split():
        if c in words:
            words[c] += 1
        else:
            words[c] = 1

numbers('kod.txt')  # Anropar funktionen som skriver ut koden
print('''
Referenslista: ''')
result = line_numbers('kod.txt', words)
for key in sorted(result):
    print(" %s %s"%(key, result[key]))
