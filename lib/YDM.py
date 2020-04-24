def ydm(yearStart, yearEnd):
    f = open('YDM.txt', 'w')
    for i in range(yearStart, yearEnd):
        for j in range(1, 32):
            x = str(i).strip() + str(j).strip()
            if len(x) != 6:
                x = x[:4] + '0' + x[4:]
                for k in range(1, 13):
                    y = str(x).strip() + str(k).strip()
                    if len(y) != 8:
                        y = y[:6] + '0' + y[6:]
                        print(y)
                        f.write(str(y).strip() + '\n')
                    else:
                        print(y)
                        f.write(str(y).strip() + '\n')

            else:
                for k in range(1, 13):
                    y = str(x).strip() + str(k).strip()
                    if len(y) != 8:
                        y = y[:6] + '0' + y[6:]
                        print(y)
                        f.write(str(y).strip() + '\n')
                    else:
                        print(y)
                        f.write(str(y).strip() + '\n')
    print("wordlist with y-d-m pattern is created")


