var methods=[2,8,69,89,12,7,13]
console.log(methods)

//Array to Stiring
var string=methods.toString()
console.log(string)

// var string_1=string.toString("*")
// console.log(string_1)

//push --> add the element to the array
methods.push("Job")
console.log(methods)

//unshift --> ADD THE element at the beginning of the array
methods.unshift("Momo")
console.log(methods)

//splice --> ADD THE element at the the random position of the array
methods.splice(3,0,21)
console.log(methods)
// 3 parameters --> 
//1st paremeter --> Index value or position
//2nd parameter --> No of element sto be deleted
//3rd parameter --> ELement to be added to the Array

// Delete the element from the Array
//pop() --> Delete the element from the end of an array
console.log(methods.pop())
console.log(methods)

//shift() --> Delete the element from the beginning of an array
methods.shift()
console.log(methods) 

//Delete the element from the specific position
delete methods[2]
console.log(methods)

//max and min
var methods_1=[2,8,69,89,12,7,13]
console.log(Math.max(methods_1))

console.log(Math.min(methods_1))

//sort
console.log(methods_1.sort())
console.log(methods_1.reverse())