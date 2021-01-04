#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    n = 0
    for i in range(list_length):
        try:
            n = my_list_1[i] / my_list_2[i]
        except TypeError:
            n = 0
            print("wrong type")
        except ZeroDivisionError:
            n = 0
            print("division by 0")
        except IndexError:
            n = 0
            print("out of range")
        finally:
            new_list.append(n)
    return (new_list)
