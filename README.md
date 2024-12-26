This Repository contains 4 different codes to check whether a number is prime or not.

prime_classic.py:
  This one is the classic old school method. I've seen many of my classmates using this method, but its total inefficient way. It basically counts every factors for the given number
from one to the number, and return true if the number has less than two factors for it. It's a straightforward brute force method, but has the highest execution time and more number
of lines

prime_silicon.py:
  This was the method I used in my lab assignments, and later my proffessor also taught us this one. This one starts checking factors from 2 instead of one, and checks until the half
of the number. The function will return False if any factor found, assuming 1 and the given number are already factors, thus avoiding redundancy. Since a numbers biggest factor is its
half, we only checks upto half. This method is proven to be 18x faster than the classical method [according to benchmark data] , also has lesser number of lines.

prime_ampere.py:
  This is similar to the one mentioned above, but this one only check factor upto square root of the given number. When I researched more about primality, I got to know about this.
But instead of using for loop, I used while loop to avoid importing sqrt from the math module. To my surprise, this improved execution time upto whopping 100 times compared to the
Silicon arcitecture, and 400x faster compared to classical method [according to benchmark data], with the same number of lines as the former one.

prime_alastas.py:
  When searching for the fastest code for primality in Github, I came across this code which is counted as the fastest code to print prime numbers. The main reason is because it elim
inates multiples of 2 and 3 first itself, which covers almost all the numbers. Also the number of iterations in the loop are also lowered by incrementing loop variable by 6, since we
already checked factorization with 2 and 3. This one is a little bit complex for rookies, but this is the fastest code for primality. It has significant increase in number of lines,
but it outperforms ampere by a factor of 1.5 to 2 in 6 digit test [see more on benchmark session]


**-----BENCHMARKING-----**

  Inorder to Benchmark these different codes, I've created the [prime_list.py] file. This is a code prints all prime numbers upto a given number, so this could be helpful in benchmarking.
The default is the 5 digit test, which prints prime numbers upto 12345. You may need to change it to 6 or 7 digits if you want to test the fastest codes, and the classical code takes 
large time even with the 5 digit test. It's also noticeable that speed gap between different codes increases exponentially as the number of digits increases.
**How to benchmark**
1. Choose which code you need to benchmark:
     Change the import statement [Line 2] to the code of your preference. It's given as prime_ampere2 as default.
2. Change the upper limit:
     Change the value upto which number you want to print the list of prime numbers. It's 12345 (5 digit test is what I call it) as default.
3. Note the time taken by the program to execute.

**-----NEW BENCHMARKING TOOL-----**
    I've added a new [prime_list_time.py] to avoid confusions in benchmarking. This code prints maximum prime numbers in a given time, unlike [prime_list] which prints upto an upper limit 
  and calculates time taken. This could be easy for comparsions.

  **----SIGNIFICANCE OF OPTIMIZATION----**
    One may argue that I made up this whole shit just to satisfy my ego with my classmates who believes their classical method is better, but this is more like a self learning for me. I've
  never thought optimization would make this drastic difference, my ampere code actually is 50 times faster than the classical method, and the alastas code overpowers the ampere code by a 
  magnitude of 2. It's significant; Imagine you're in a coding competition or job interview or a real life situation and some guy makes a code that's 50 times faster than you...

    I'm also adding a presentation with the benchmark results

  [Benchmark.pptx](https://github.com/user-attachments/files/18253624/Benchmark.pptx)
