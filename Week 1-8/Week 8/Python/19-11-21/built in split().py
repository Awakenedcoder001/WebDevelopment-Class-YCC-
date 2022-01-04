
fact="Sonam Tobgay Had a Crush on Thinley Wangmo" 
print(fact.split()) 
 
fact="Sonam Tobgay Had a Crush on Thinley Wangmo" 
print(fact.split('a')) 
 
import re 
fact="Sonam Tobgay Had a Crush on Thinley Wangmo" 
pattern="a" 
result=re.split(pattern,fact) 
print(result) 
 
for elements in result: 
 print(elements)

Thazay, [19.11.21 12:35]
['Sonam', 'Tobgay', 'Had', 'a', 'Crush', 'on', 'Thinley', 'Wangmo'] 
['Son', 'm Tobg', 'y H', 'd ', ' Crush on Thinley W', 'ngmo'] 
['Son', 'm Tobg', 'y H', 'd ', ' Crush on Thinley W', 'ngmo'] 
Son 
m Tobg 
y H 
d 
 Crush on Thinley W 
ngmo