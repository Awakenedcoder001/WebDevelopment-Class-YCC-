var Pema = {
    age : 26 ,
    Gender : 'male',
    Qualification : {
        Degree : "Standford_University",
        GPA     : 3.6,
        Course :   "Web_development",
    }
}
console.log(Pema)
delete Pema.Qualification.Course
console.log(Pema)

