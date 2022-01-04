/*(  ) => {
    let a = 100;
    let b = 200;
    console.log(a+b);
}
operation( )
*/
//Arrow function with Arguments object
var operation = (firstname,secondname) => {
    fullname=   firstname + "" +secondname;
    console.log("THE NAME OF THE PERSON IS:",fullname);
}
operation("sonam", "Todlay")
