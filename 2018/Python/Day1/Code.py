def calculate(input):
    return sum([int(number) for number in input.split(", ")])

def calculate_second(input):
    input = input.split(", ")
    length = len(input)
    index = 0
    frequency = 0
    frequencies = set([frequency])
    while True:
        frequency = frequency + int(input[index % length])
        if frequency not in frequencies:
            frequencies.add(frequency)
            index = index + 1
        else:
            return frequency
