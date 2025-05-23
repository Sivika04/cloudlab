from collections import Counter
def count_elements(data):
    return Counter(data)

   
    my_string = "cloudlab"
    string_counts = count_elements(my_string)
    print("String character counts:", string_counts)
