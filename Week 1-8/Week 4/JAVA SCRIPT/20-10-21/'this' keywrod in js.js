 var student_info =
 {
        name: 'Singye',
        age : 23,
        salarym: 25000,
        relation_status: "single",
        designation : "student",
        display : function()
        {
            console.log(`This name is of : ${this.name} 
            and age is :${this.age} 
            then paid salary is : ${this.salary} 
            next comes: ${this.relation_status}`)
        }
 }
 student_info.display()