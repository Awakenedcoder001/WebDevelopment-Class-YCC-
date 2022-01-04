Thinley Tobgay, [26.10.21 09:49]
class RBA{
    static army= "Royal BHutan Army";
    constructor(name, age, gender){
        this.name=name;
        this.age=age;
        this.gender=gender;
    }
    display(){
        console.log(`${this.name}, ${this.age}, ${this.gender}`)
    }
    static display(){
        console.log(`${this.army}`)
    }
}
var obj1= new RBA("jigme", 41, "male");
RBA.display();
obj1.display();
class Police extends RBA{
}
const obj2= new Police("rambo", 15, "male");
obj2.display();

Thinley Tobgay, [26.10.21 09:52]
class RBA{
    static army= "Royal BHutan Army";
    constructor(name, age, gender){
        this.name=name;
        this.age=age;
        this.gender=gender;
    }
    display(){
        console.log(`${this.name}, ${this.age}, ${this.gender}`)
    }
    static display(){
        console.log(`${this.army}`)
    }
}
var obj1= new RBA("jigme", 41, "male");
RBA.display();
obj1.display();
class Police extends RBA{
}
const obj2= new Police("rambo", 15, "male");
obj2.display();