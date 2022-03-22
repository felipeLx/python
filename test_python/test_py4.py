# check if the firt word end with the second argument
def endwithstring(string, ending):
    return string.endswith(ending)
print(endwithstring('duck', 'ck'))

# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed
def sping_words(sentence):
    # return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())

print(sping_words("Hello World"))

# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
def check_is_narcis_number(your_number):
    your_numbers = str(your_number)
    power = len(your_numbers)
    your_sum = 0
    for number in your_numbers:
        your_sum += pow(int(number), power)
    if your_sum == your_number:
        return True
    return False

def printintstr(array):
    return '" {} "'.format(array.split(','))

print(printintstr([1,2,3])) 