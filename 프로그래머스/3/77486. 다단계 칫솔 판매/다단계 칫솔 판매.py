def to_parents(parents, moneys, name, earn_money):
    current = name
    while current != "":
        earn_for_parent = earn_money // 10
        moneys[current] += earn_money - earn_for_parent
        earn_money = earn_for_parent
        current = parents[current]
        if earn_money == 0:
            break


def solution(enroll, referral, seller, amount):
    money = {name: 0 for name in enroll}
    money["-"] = 0
    parent = {enroll[i]: referral[i] for i in range(len(enroll))}
    parent["-"] = ""

    for i in range(len(seller)):
        earn = amount[i] * 100
        to_parents(parent, money, seller[i], earn)

    return [money[name] for name in enroll]