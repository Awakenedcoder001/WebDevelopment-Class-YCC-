Thazay, [18.11.21 14:34]
#meta Characters 
import re 
Thazay=input("Enter the pattern to be match:") 
Khandu=input("Enter the string:") 
Result=re.finditer(Thazay,Khandu) 
for icecream in Result: 
 print(f'{icecream.start()} & {icecream.end()} and {icecream.group()}') 
 
#output 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[abc] 
# Enter the string:Karma sangay is good 
# 1 & 2 and a 
# 4 & 5 and a 
# 7 & 8 and a 
# 10 & 11 and a 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[^abc] 
# Enter the string:Karma sangay is good 
# 0 & 1 and K 
# 2 & 3 and r 
# 3 & 4 and m 
# 5 & 6 and 
# 6 & 7 and s 
# 8 & 9 and n 
# 9 & 10 and g 
# 11 & 12 and y 
# 12 & 13 and 
# 13 & 14 and i 
# 14 & 15 and s 
# 15 & 16 and 
# 16 & 17 and g 
# 17 & 18 and o 
# 18 & 19 and o 
# 19 & 20 and d 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[0-9] 
# Enter the string:karma mobile number is 17420300 and khadu number is 77478402 
# 23 & 24 and 1 
# 24 & 25 and 7 
# 25 & 26 and 4 
# 26 & 27 and 2 
# 27 & 28 and 0 
# 28 & 29 and 3 
# 29 & 30 and 0 
# 30 & 31 and 0 
# 52 & 53 and 7 
# 53 & 54 and 7 
# 54 & 55 and 4 
# 55 & 56 and 7 
# 56 & 57 and 8 
# 57 & 58 and 4 
# 58 & 59 and 0 
# 59 & 60 and 2 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[^0-9] 
# Enter the string:karma mobile number is 17420300 and khadu number is 77478402 
# 0 & 1 and k 
# 1 & 2 and a 
# 2 & 3 and r 
# 3 & 4 and m 
# 4 & 5 and a 
# 5 & 6 and 
# 6 & 7 and m 
# 7 & 8 and o 
# 8 & 9 and b 
# 9 & 10 and i 
# 10 & 11 and l 
# 11 & 12 and e 
# 12 & 13 and 
# 13 & 14 and n 
# 14 & 15 and u 
# 15 & 16 and m 
# 16 & 17 and b 
# 17 & 18 and e 
# 18 & 19 and r 
# 19 & 20 and 
# 20 & 21 and i 
# 21 & 22 and s 
# 22 & 23 and 
# 31 & 32 and 
# 32 & 33 and a 
# 33 & 34 and n 
# 34 & 35 and d 
# 35 & 36 and 
# 36 & 37 and k 
# 37 & 38 and h 
# 38 & 39 and a 
# 39 & 40 and d 
# 40 & 41 and u 
# 41 & 42 and 
# 42 & 43 and n 
# 43 & 44 and u 
# 44 & 45 and m 
# 45 & 46 and b 
# 46 & 47 and e 
# 47 & 48 and r 
# 48 & 49 and 
# 49 & 50 and i 
# 50 & 51 and s 
# 51 & 52 and 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[a-z] 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 8 & 9 and o 
# 9 & 10 and b 
# 10 & 11 and i 
# 11 & 12 and l 
# 12 & 13 and e 
# 15 & 16 and u 
# 16 & 17 and m 
# 17 & 18 and b 
# 18 & 19 and e 
# 19 & 20 and r 
# 21 & 22 and i 
# 22 & 23 and s 
# 34 & 35 and n 
# 35 & 36 and d 
# 38 & 39 and h 
# 39 & 40 and a 
# 40 & 41 and d 
# 41 & 42 and u 
# 44 & 45 and u 
# 45 & 46 and m 
# 46 & 47 and b 
# 47 & 48 and e 
# 50 & 51 and i 
# 51 & 52 and s 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[^a-z] 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 0 & 1 and K 
# 1 & 2 and A 
# 2 & 3 and R 
# 3 & 4 and M 
# 4 & 5 and A 
# 5 & 6 and 
# 6 & 7 and 
# 7 & 8 and M 
# 13 & 14 and 
# 14 & 15 and N 
# 20 & 21 and 
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
# 36 & 37 and 
# 37 & 38 and K 
# 42 & 43 and 
# 43 & 44 and N 
# 48 & 49 and R 
# 49 & 50 and 
# 52 & 53 and 
# 53 & 54 and 7 
# 54 & 55 and 7 
# 55 & 56 and 4 
# 56 & 57 and 7 
# 57 & 58 and 8 
# 58 & 59 and 4 
# 59 & 60 and 0 
# 60 & 61 and 2 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[A-Z] 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 0 & 1 and K 
# 1 & 2 and A 
# 2 & 3 and R 
# 3 & 4 and M 
# 4 & 5 and A 
# 7 & 8 and M 
# 14 & 15 and N 
# 33 & 34 and A 
# 37 & 38 and K 
# 43 & 44 and N 
# 48 & 49 and R 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[^A-Z] 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 5 & 6 and 
# 6 & 7 and 
# 8 & 9 and o 
# 9 & 10 and b 
# 10 & 11 and i 
# 11 & 12 and l 
# 12 & 13 and e 
# 13 & 14 and 
# 15 & 16 and

Thazay, [18.11.21 14:34]
u 
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
# 34 & 35 and n 
# 35 & 36 and d 
# 36 & 37 and 
# 38 & 39 and h 
# 39 & 40 and a 
# 40 & 41 and d 
# 41 & 42 and u 
# 42 & 43 and 
# 44 & 45 and u 
# 45 & 46 and m 
# 46 & 47 and b 
# 47 & 48 and e 
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
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[A-Za-z] 
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
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[^A-Za-z] 
# Enter the string:KARMA  Mobile Number is 17420300 And Khadu NumbeR is 77478402 
# 5 & 6 and 
# 6 & 7 and 
# 13 & 14 and 
# 20 & 21 and 
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
# 36 & 37 and 
# 42 & 43 and 
# 49 & 50 and 
# 52 & 53 and 
# 53 & 54 and 7 
# 54 & 55 and 7 
# 55 & 56 and 4 
# 56 & 57 and 7 
# 57 & 58 and 8 
# 58 & 59 and 4 
# 59 & 60 and 0 
# 60 & 61 and 2 
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[A-Za-z0-9] 
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
 
# D:\Python>python "Meta Characters.py" 
# Enter the pattern to be match:[^A-Za-z0-9] 
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