class subtract1
{
    constructor(num1,num2){
        this.num1 = num1;
        this.num2 = num2;
    }

    subtractionOperation()
    {
        this.totalsubtract1 = this.num1-this.num2;
    }

    display()
    {
        console.log(`the subtraction of two numbers is ${this.totalSubract1}`);

    }

}
var final= new subtract1(10,20);
final.subtractionOperation();
final.display();