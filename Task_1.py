def calc_salt(weight):
    try:
        if isinstance(weight, str):
            weight = int(weight)
        result = weight / 1000 * 10
    except Exception as e:
        print(e)
        result = 0.0
    return result

print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))




