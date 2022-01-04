class staticMethod{
 static country="bhutan";
 static course="commerce";

    static display(){
        console.log(this.course);
        console.log(staticMethod.country);

    }

}
// Inorder to declare as static method we must include pre-fix called as satic (keywords)
const obj1 = new staticMethod();
// if we tery to access static method using object reference it will return an error
// Obj1,display();
// We can access static method only by using class name.
staticMethod.display();