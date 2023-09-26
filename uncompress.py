def uncompress(str):
    numbers = '0123456789'
    result = []

    i = 0
    j = 0
    while j < len(str):
        if str[j] in numbers:
            j += 1
        else:
            num = int(str[i:j])
            result.append(str[j] * num)
            j += 1
            i = j

    return ''.join(result)
