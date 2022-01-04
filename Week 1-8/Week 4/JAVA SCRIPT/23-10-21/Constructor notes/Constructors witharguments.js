class CrickterDetails{
    constructor(name,average){
        console.log("inside the constructor");
       
       console.log(name);
       console.log(average);
       console.log("leaving the constructor");
    }
}
console.log(" executing LineNumber 1");
new CrickterDetails("pema", 24.5);//objection creation 
new CrickterDetails("wangdi", 64.5);//objection creation 


console.log("program executed");

constructor with argument