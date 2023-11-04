def csillag_vonal():
    for _ in range(24):
        print("*", end="")
    print()


def nyugta():
    csillag_vonal()
    print("*", end="")
    print('{:^21}'.format('Nyugta'), "*")
    csillag_vonal()


def ceg():
    csillag_vonal()
    print("*", end="")
    print('{:^21}'.format('Cég'), "*")
    csillag_vonal()


def alairas():
    alair = "_________"
    print(alair, '{:>14}'.format(alair), "")
    print("  Dátum", '{:>13}'.format("Név"), "")
