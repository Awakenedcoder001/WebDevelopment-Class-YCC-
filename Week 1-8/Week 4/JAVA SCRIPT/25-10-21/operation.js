class sum1{ 
    constructor(num1,num2){ 
        this.num1=num1; 
        this.num2=num2; 
    } 
    addOperation(){ 
        this.totalSum=this.num1+this.num2;   
    } 
    display(){ 
    console.log(`The total sum of two numbers is ${this.totalSum}`); 
    } 
} 
var finalSum=new sum1(100, 20); 
finalSum.addOperation(); 
finalSum.display(); 
 
class subt1{ 
    constructor(num1,num2){ 
        this.num1=num1; 
        this.num2=num2; 
    } 
    subtOperation(){ 
        this.totalSubt=this.num1-this.num2;   
    } 
    display(){ 
    console.log(`The total remain of two numbers is ${this.totalSubt}`); 
    } 
} 
var finalSubt=new subt1(100, 20); 
finalSubt.subtOperation(); 
finalSubt.display(); 
 
class multi1{ 
    constructor(num1,num2){ 
        this.num1=num1; 
        this.num2=num2; 
    } 
    multiOperation(){ 
        this.totalMulti=this.num1*this.num2;   
    } 
    display(){ 
    console.log(`The total of two numbers is ${this.totalMulti}`); 
    } 
} 
var finalMulti=new multi1(100, 20); 
finalMulti.multiOperation(); 
finalMulti.display(); 
 
class expo1{ 
    constructor(num1,num2){ 
        this.num1=num1; 
        this.num2=num2; 
    } 
    expoOperation(){ 
        this.totalExpo=this.num1%this.num2;   
    } 
    display(){ 
    console.log(`The total of two numbers is ${this.totalExpo}`); 
    } 
} 
var finalExpo=new expo1(100, 20); 
finalExpo.expoOperation(); 
finalExpo.display(); 
 
class div1{ 
    constructor(num1,num2){ 
        this.num1=num1; 
        this.num2=num2; 
    } 
    divOperation(){ 
        this.totalDiv=this.num1/this.num2;   
    } 
    display(){ 
    console.log(`The total of two numbers is ${this.totalDiv}`); 
    } 
} 
var finalDiv=new div1(100, 20); 
finalDiv.divOperation(); 
finalDiv.display();