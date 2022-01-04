Thinley Tobgay, [25.10.21 12:15]
class WebDevelopment{
    //following two is static varables
    static nationalLanguage="Dzongkha";
    static nationality="Bhutaneses";
    //below is instance varable initalization
    constructor(name, did,average){
      // initailzation of variable to instance varables       
        this.name=name;
        this.did=did;
        this.average=average;
    }
    display(){ // instance varable method
        console.log(`name = ${this.name}, DID = ${this.did}, avarage = ${this.average}`);
    }
    static display(){ //static varable method
        //we cannot access the instance variables inside static method using this keyword.
        // console.log(`name = ${this.name}, DID = ${this.did}, avarage = ${this.average}`);
        console.log(WebDevelopment.nationalLanguage);
        console.log(this.nationality)
    }
}
const obj1 = new WebDevelopment("pema", "DS(42)20-213453", 45);
// accessing the static vaiable  inside static method
WebDevelopment.display();
// accessing the instance vaiable  inside instance method
obj1.display();