var person={
    name: "singye",
    salary: 25000,
    age: 16,
}
person.display = function()
{
console.log(`name is : ${this.name} having a salary of : ${this.salary} who is about : ${this.age} years old`)

}
console.log(person.display)
person.display()
