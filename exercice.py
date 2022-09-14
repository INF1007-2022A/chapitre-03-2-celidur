#!/usr/bin/env python


def dissipated_power(voltage, resistance):
    return voltage ** 2 / resistance


def orthogonal(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] == 0


def average(values):
    # calcul the average of positive values in values
    # return 0 if there is no positive value
    total = 0
    count = 0
    for value in values:
        if value >= 0:
            total += value
            count += 1
    if count == 0:
        return 0
    return total / count


def bills(value):
    twenties, value = value // 20, value % 20
    tens, value = value // 10, value % 10
    fives, value = value // 5, value % 5
    ones = value
    return twenties, tens, fives, ones


def format_base(value, base, digit_letters):
    # Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
    # `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    result = ""
    abs_value = abs(value)
    while abs_value != 0:
        abs_value, digit = divmod(abs_value, base)
        result += digit_letters[digit]
    if value < 0:
        result += "-"
    return result[::-1]


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
    print(format_base(-42, 16, "0123456789ABCDEF"))
