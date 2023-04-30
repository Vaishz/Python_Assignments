def most_frequent(string):
    frequency={}
    for char in string:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1

    sorted_frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

    for key, value in sorted_frequency.items():
        print(key, '=', value, end=' ')

