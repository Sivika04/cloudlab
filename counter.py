from collections import Counter
def count_elements(data):
    return Counter(data)
if __name__ == "__main__":
   
    my_string = "abracadabra"
    string_counts = count_elements(my_string)
    print("String character counts:", string_counts)
