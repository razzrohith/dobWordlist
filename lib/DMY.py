def dmy(yearStart, yearEnd):
    f = open('DMY.txt', 'w')
    for i in range(1, 32):
        x = str(i)
        if len(x) != 2:
            x = x[:0] + '0' + x[0:]
            for j in range(1, 13):
                y = str(x).strip() + str(j).strip()
                if len(y) != 4:
                    y = y[:2] + '0' + y[2:]
                    for k in range(yearStart, yearEnd):
                        z = str(y).strip() + str(k).strip()
                        print(z)
                        f.write(str(z).strip() + '\n')
                else:
                    for k in range(yearStart, yearEnd):
                        z = str(y).strip() + str(k).strip()
                        print(z)
                        f.write(str(z).strip() + '\n')

        else:
            for j in range(1, 13):
                y = str(x).strip() + str(j).strip()
                if len(y) != 4:
                    y = y[:2] + '0' + y[2:]
                    for k in range(yearStart, yearEnd):
                        z = str(y).strip() + str(k).strip()
                        f.write(str(z).strip() + '\n')
                        print(z)
                else:
                    for k in range(yearStart, yearEnd):
                        z = str(y).strip() + str(k).strip()
                        f.write(str(z).strip() + '\n')
                        print(z)
    print("wordlist with d-m-y pattern is created")


