n range(0, 99):
    if n % 10 > n / 10:
        if n < 89:
            print("{:02d}, ".format(n), end='')
        else:
            print("{:02d}".format(n))
