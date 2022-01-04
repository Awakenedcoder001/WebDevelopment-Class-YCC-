class DSP{
    static course="web Development";
    static country="bhutan";//static varable should always be defined out side the method
    constructor(name, age, bloodG){
        this.name=name;
        this.age=age;
        this.bloodG=bloodG; 
    }
    display(){
        console.log(`name = ${this.name}, Age = ${this.age}, bloodG = ${this.bloodG}`);
        //accessing static variable using two ways
        console.log(DSP.course);
        //console.log(this.country);
    }
}
var Obj1= new DSP("pema", 14,"B");
Obj1.display();
var obj2 = new DSP("dorji", 24, "A+");
obj2.display();