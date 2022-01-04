Thinley Tobgay, [25.10.21 09:38]
class sum1{
    constructor(num1,num2){
        this.num1=num1;
        this.num2=num2;
    }
    addOperation(){
        this.totalSum=this.num1+this.num2;  
    }
    display(){
    console.log(`the total sum of two numbers is ${this.totalSum}`);
    }
}
var finalSum=new sum1(10, 20);
finalSum.addOperation();
finalSum.display();