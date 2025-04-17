# Homework:

# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers. 
# Divide the range among multiple threads to parallelize the prime checking process. 
# Each thread should be responsible for checking a subset of the range, 
# and the main program should print the list of prime numbers found.
import threading

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
    
def check_prime(start, end, prime_numbers_list: list):
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers_list.append(num)


def threaded_check_prime(start_range, end_range, num_threads = 4):
    threads = []
    divide_size = (end_range - start_range) // num_threads
    all_primes = []
    for i in range(num_threads):
        start = start_range + i * divide_size
        end = start_range + (i + 1) * divide_size if i != num_threads - 1 else end_range
        temp = []
        t = threading.Thread(target=check_prime, args=(start, end , temp))
        threads.append((t, temp))
        t.start()
    for t, result in threads:
        t.join()
        all_primes.extend(result)
    print("Prime numbers: ", sorted(all_primes))

if __name__ == "__main__":
    threaded_check_prime(1, 111, num_threads=4)






# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text. 
# Implement a threaded solution to count the occurrence of each word in the file.
#  Each thread should process a portion of the file, 
# and the main program should display a summary of word occurrences across all threads.
import string
import threading
from collections import defaultdict

def clean_text(text:str):
    for i in text:
            if i in string.punctuation and i != "'":
                text = text.replace(i, " ")
    return text

def count_words(lines, word_dict: list):
    local_dict = defaultdict(int)
    for line in lines:
        line = clean_text(line)
        for word in line.split():
            local_dict[word.lower()] += 1
    word_dict.append(local_dict)

    
def threaded_word_count(filename, num_threads = 4):
    with open(filename, "r", encoding="utf-8") as f:
          lines = f.readlines()
    devite_size = len(lines) // num_threads
    thresds = []


    for i in range(num_threads):
        start = i * devite_size 
        end = (i + 1) * devite_size if i != num_threads - 1 else len(lines)
        text = lines[start:end]
        temp = []
        t = threading.Thread(target=count_words, args=(text, temp))
        thresds.append((t, temp))
        t.start()
    
    final_result = defaultdict(int)

    for t, temp in thresds:
        t.join()
        for local_dict in temp:
             for word, count in local_dict.items():
                  final_result[word] += count

    for word, count in sorted(final_result.items(), key = lambda x: x[1], reverse=True):
         print(f"{word} --> [{count}]")

if __name__ == "__main__":
     threaded_word_count("test.txt", num_threads = 4)

          
             
     
