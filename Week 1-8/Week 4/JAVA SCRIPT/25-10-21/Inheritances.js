class RBA{ 
    static Army="Royal Bhutan Army"; 
    constructor(name,age,gender){ 
        this.name = name; 
        this.age = age; 
        this.gender = gender; 
    } 
    display(){ 
        console.log(`Name is ${this.name}, Age is ${this.age}, Gender is ${this.gender}`); 
    } 
    static display(){ 
        console.log(`This army belong to ${this.army}`) 
    } 
    var obj1=new RBA(Jigme,45,Male) 
    RBA display() //Execute Static Method 
    obj1.display() //Execute Static Method 
}