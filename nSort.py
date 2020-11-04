def intToArray(number):
    # takes a (decimal) int and returns an array of the array and base 10 e.g. 123 -> [[1,2,3], 10]
    temp = str(number)
    final = [[], 10]

    for index, value in enumerate(temp):
        final[0].append(value);

    return final


def basechange(number, base, original_base=10):
    sum = 0
    #reverse number for enumerate (for clean code, not efficiency as this increases runtime likely by n)
    number = number[::-1]

    #recreate a base 10 sum (ultimately arbitrary except for human understanding)
    for power, value in enumerate(number):
        sum += value * (original_base ** (power))

    result = []
    power = 0

    while sum > 0:
        power_value = (sum % (base**(power+1)))
        # result.append(int(power_value/(base**power)))
        result.insert(0, int(power_value/(base**power)))
        sum -= power_value
        power +=1

    # result = result[::-1]
    print(result)

    return [result, base]





