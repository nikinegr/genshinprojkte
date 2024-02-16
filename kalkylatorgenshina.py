while True:
    qwert = input('dla vozvishenia persa+/dla vozvishenia oruzhia i kristalov-')
    if qwert == "+":
        a = int(input('vvedit kolovo leg'))
        s = int(input('vvedit kolovo epik'))
        d = int(input('vvedit kolovo redkih'))
        f = int(input('vvedit kolovo odich'))
        g = a * 3 + s
        h = g * 3 + d
        j = h * 3 + f
        res = input('+/-')
        if res == '+':
            z = int(input('vvedit nuzhnoe kolovo leg'))
            x = int(input('vvedit nuzhnoe kolovo epik'))
            c = int(input('vvedit nuzhnoe kolovo redkih'))
            v = int(input('vvedit nuzhnoe kolovo odich'))
            b = z * 3 + x
            n = b * 3 + c
            m = n * 3 + v
            y = m - j
            if j > m:
                print(f'ti v pluse na {y}')
            if j < m:
                print(f"nyzhno {y}")
        else:
            print(f"vsego odich {j}")
    ex = input('exit')
    if ex == "exit":
        import menu
    elif qwert == '-':
        a = int(input('vvedit kolovo 1 formi'))
        s = int(input('vvedit kolovo 2 formi'))
        d = int(input('vvedit kolovo 3 formi'))
        g = a * 3 + s
        h = g * 3 + d
        res = input('+/-')
        if res == '+':
            z = int(input('vvedit nuzhnoe kolovo 1 formi'))
            x = int(input('vvedit nuzhnoe kolovo 2 formi'))
            c = int(input('vvedit nuzhnoe kolovo 3 formi'))
            b = z * 3 + x
            n = b * 3 + c
            y = h - n
            if n > h:
                print(f"nyzhno 3 formi {y}")
            if n < h:
                print(f'ti v pluse na {y}')

        else:
            print(f"vsego 3 formi {h}")
    ex = input('exit')
    if ex == "exit":
        import menu




