Thinley Tobgay, [25.10.21 11:42]
class staticMethod{
    static country="Bhutan";
    static course="Web";
    // in order to declear as static method we must include pre-fix called as static (keyword)
    static display(){
        // accessing static variable in two ways: 
        // using this keyword 
        // using class name 
        console.log(this.course);
        console.log(staticMethod.country);
    }
}
const obj1=new staticMethod();
//if we try to acess static method using object refrences it will return an error.
// obj1.display();
// we can acess static method noly by using class name.
staticMethod.display();