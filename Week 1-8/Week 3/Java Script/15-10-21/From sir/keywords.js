// Variable should always start with _ or $ or alphabets
var $num=10;
console.log($num);

var _num=100;
console.log(_num); 

var num="WEB DEVELOPMENT"
console.log(num)

//var 1num=25;
//console.log(1num) --> Invalid or un expected token

// RULE 2: can have a combination of letters , underscores ,numbers
var num=10;
console.log(num)

var num_1 = 1000;
console.log(num_1)

// RULE 3: CAN NOT CONTAIN KEYWORDS
// var = 10;
// console.log(var) --> Syntax error

// RULE 4: VARIABLE NAMES ARE CASE SENSITIVE
var Num = 100;
console.log(Num)

var num=10;
console.log(num)

// APART FROM _ AND $ no other special characters are allowed
var !num=100; --> ERROR --> UNCEPTED TOKEN '!'
console.log(!num)
