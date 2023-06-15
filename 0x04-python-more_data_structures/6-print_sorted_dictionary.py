#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in range(len(a_dictionary)):
        print(f"{list(a_dictionary.keys())[i]}: {list(a_dictionary.values())[i]}")


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
