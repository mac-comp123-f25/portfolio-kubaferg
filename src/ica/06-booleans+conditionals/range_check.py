def range_limit (num):
    if num > 1 and num < 10:
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    assert range_limit(8) == True
    assert range_limit(-1) == False
    assert range_limit(50) == False
    print("All tests passed")