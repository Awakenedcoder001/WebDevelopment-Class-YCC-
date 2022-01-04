class CrickterDetails{
    constructor(name,average){
        console.log("inside the constructor");
        var pname = name
        var average=average
       console.log("leaving the constructor");
    }

display(){
    console.log(`name is ${name}and average is ${average}`);

}

}   

console.log(" executing LineNumber 1");
const finalResult=new CrickterDetails("pema", 24.5);//objection creation 


new CrickterDetails("wangdi", 64.5);//objection creation 


console.log("program executed");
