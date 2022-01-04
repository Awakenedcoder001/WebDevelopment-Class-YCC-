Thazay, [18.11.21 15:39]
#predefind meta Characters 
#(\s[^A-Za-z0-9] \S[^A-Za-z0-9]) 
#(\d[0-9] \D[^0-9] ) 
#(\w[A-Za-z0-9] \W[^A-Za-z0-9]) 
# .All the characters in the string 
import re 
Thazay=input("Enter the pattern to be match:") 
Khandu=input("Enter the string:") 
Result=re.finditer(Thazay,Khandu) 
for icecream in Result: 
 print(f'{icecream.start()} & {icecream.end()} and {icecream.group()}') 
#output 
 
# D:\Python>python predefined.py 
# Enter the pattern to be match:\s 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 5 & 6 and 
# 6 & 7 and 
# 13 & 14 and 
# 20 & 21 and 
# 23 & 24 and 
# 32 & 33 and 
# 36 & 37 and 
# 42 & 43 and 
# 49 & 50 and 
# 52 & 53 and 
 
# D:\Python>python predefined.py 
# Enter the pattern to be match:\S 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 0 & 1 and K 
# 1 & 2 and A 
# 2 & 3 and R 
# 3 & 4 and M 
# 4 & 5 and A 
# 7 & 8 and M 
# 8 & 9 and o 
# 9 & 10 and b 
# 10 & 11 and i 
# 11 & 12 and l 
# 12 & 13 and e 
# 14 & 15 and N 
# 15 & 16 and u 
# 16 & 17 and m 
# 17 & 18 and b 
# 18 & 19 and e 
# 19 & 20 and r 
# 21 & 22 and i 
# 22 & 23 and s 
# 24 & 25 and 1 
# 25 & 26 and 7 
# 26 & 27 and 4 
# 27 & 28 and 2 
# 28 & 29 and 0 
# 29 & 30 and 3 
# 30 & 31 and 0 
# 31 & 32 and 0 
# 33 & 34 and A 
# 34 & 35 and n 
# 35 & 36 and d 
# 37 & 38 and K 
# 38 & 39 and h 
# 39 & 40 and a 
# 40 & 41 and d 
# 41 & 42 and u 
# 43 & 44 and N 
# 44 & 45 and u 
# 45 & 46 and m 
# 46 & 47 and b 
# 47 & 48 and e 
# 48 & 49 and R 
# 50 & 51 and i 
# 51 & 52 and s 
# 53 & 54 and 7 
# 54 & 55 and 7 
# 55 & 56 and 4 
# 56 & 57 and 7 
# 57 & 58 and 8 
# 58 & 59 and 4 
# 59 & 60 and 0 
# 60 & 61 and 2 
 
# D:\Python>python predefined.py 
# Enter the pattern to be match:\d 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 24 & 25 and 1 
# 25 & 26 and 7 
# 26 & 27 and 4 
# 27 & 28 and 2 
# 28 & 29 and 0 
# 29 & 30 and 3 
# 30 & 31 and 0 
# 31 & 32 and 0 
# 53 & 54 and 7 
# 54 & 55 and 7 
# 55 & 56 and 4 
# 56 & 57 and 7 
# 57 & 58 and 8 
# 58 & 59 and 4 
# 59 & 60 and 0 
# 60 & 61 and 2 
 
# D:\Python>python predefined.py 
# Enter the pattern to be match:\D 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 0 & 1 and K 
# 1 & 2 and A 
# 2 & 3 and R 
# 3 & 4 and M 
# 4 & 5 and A 
# 5 & 6 and 
# 6 & 7 and 
# 7 & 8 and M 
# 8 & 9 and o 
# 9 & 10 and b 
# 10 & 11 and i 
# 11 & 12 and l 
# 12 & 13 and e 
# 13 & 14 and 
# 14 & 15 and N 
# 15 & 16 and u 
# 16 & 17 and m 
# 17 & 18 and b 
# 18 & 19 and e 
# 19 & 20 and r 
# 20 & 21 and 
# 21 & 22 and i 
# 22 & 23 and s 
# 23 & 24 and 
# 32 & 33 and 
# 33 & 34 and A 
# 34 & 35 and n 
# 35 & 36 and d 
# 36 & 37 and 
# 37 & 38 and K 
# 38 & 39 and h 
# 39 & 40 and a 
# 40 & 41 and d 
# 41 & 42 and u 
# 42 & 43 and 
# 43 & 44 and N 
# 44 & 45 and u 
# 45 & 46 and m 
# 46 & 47 and b 
# 47 & 48 and e 
# 48 & 49 and R 
# 49 & 50 and 
# 50 & 51 and i 
# 51 & 52 and s 
# 52 & 53 and 
 
# D:\Python>python predefined.py 
# Enter the pattern to be match:\w 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 0 & 1 and K 
# 1 & 2 and A 
# 2 & 3 and R 
# 3 & 4 and M 
# 4 & 5 and A 
# 7 & 8 and M 
# 8 & 9 and o 
# 9 & 10 and b 
# 10 & 11 and i 
# 11 & 12 and l 
# 12 & 13 and e 
# 14 & 15 and N 
# 15 & 16 and u 
# 16 & 17 and m 
# 17 & 18 and b 
# 18 & 19 and e 
# 19 & 20 and r 
# 21 & 22 and i 
# 22 & 23 and s 
# 24 & 25 and 1 
# 25 & 26 and 7 
# 26 & 27 and 4 
# 27 & 28 and 2 
# 28 & 29 and 0 
# 29 & 30 and 3 
# 30 & 31 and 0 
# 31 & 32 and 0 
# 33 & 34 and A 
# 34 & 35 and n 
# 35 & 36 and d 
# 37 & 38 and K 
# 38 & 39 and h 
# 39 & 40 and a 
# 40 & 41 and d 
# 41 & 42 and u 
# 43 & 44 and N 
# 44 & 45 and u 
# 45 & 46 and m 
# 46 & 47 and b 
# 47 & 48 and e 
# 48 & 49 and R 
# 50 & 51 and i 
# 51 & 52 and s 
# 53 & 54 and 7 
# 54 & 55 and 7 
# 55 & 56 and 4 
# 56 & 57 and 7 
# 57 & 58 and 8 
# 58 & 59 and 4 
# 59 & 60 and 0 
# 60 & 61 and 2 
 
# D:\Python>python predefined.py 
# Enter the pattern to be match:\W 
# Enter the

Thazay, [18.11.21 15:39]
string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 5 & 6 and 
# 6 & 7 and 
# 13 & 14 and 
# 20 & 21 and 
# 23 & 24 and 
# 32 & 33 and 
# 36 & 37 and 
# 42 & 43 and 
# 49 & 50 and 
# 52 & 53 and 
 
# D:\Python>python predefined.py 
# Enter the pattern to be match:. 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 0 & 1 and K 
# 1 & 2 and A 
# 2 & 3 and R 
# 3 & 4 and M 
# 4 & 5 and A 
# 5 & 6 and 
# 6 & 7 and 
# 7 & 8 and M 
# 8 & 9 and o 
# 9 & 10 and b 
# 10 & 11 and i 
# 11 & 12 and l 
# 12 & 13 and e 
# 13 & 14 and 
# 14 & 15 and N 
# 15 & 16 and u 
# 16 & 17 and m 
# 17 & 18 and b 
# 18 & 19 and e 
# 19 & 20 and r 
# 20 & 21 and 
# 21 & 22 and i 
# 22 & 23 and s 
# 23 & 24 and 
# 24 & 25 and 1 
# 25 & 26 and 7 
# 26 & 27 and 4 
# 27 & 28 and 2 
# 28 & 29 and 0 
# 29 & 30 and 3 
# 30 & 31 and 0 
# 31 & 32 and 0 
# 32 & 33 and 
# 33 & 34 and A 
# 34 & 35 and n 
# 35 & 36 and d 
# 36 & 37 and 
# 37 & 38 and K 
# 38 & 39 and h 
# 39 & 40 and a 
# 40 & 41 and d 
# 41 & 42 and u 
# 42 & 43 and 
# 43 & 44 and N 
# 44 & 45 and u 
# 45 & 46 and m 
# 46 & 47 and b 
# 47 & 48 and e 
# 48 & 49 and R 
# 49 & 50 and 
# 50 & 51 and i 
# 51 & 52 and s 
# 52 & 53 and 
# 53 & 54 and 7 
# 54 & 55 and 7 
# 55 & 56 and 4 
# 56 & 57 and 7 
# 57 & 58 and 8 
# 58 & 59 and 4 
# 59 & 60 and 0 
# 60 & 61 and 2 