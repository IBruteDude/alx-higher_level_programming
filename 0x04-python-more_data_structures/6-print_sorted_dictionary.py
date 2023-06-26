#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in range(len(a_dictionary)):
        print(f"{list(a_dictionary.keys())[i]}:"
              f" {list(a_dictionary.values())[i]}")

if __name__ == "__main__":
    a_dictionary = {
        'language': "C",
        'Number': 89,
        'track': "Low level",
        'ids': [1, 2, 3]
    }
