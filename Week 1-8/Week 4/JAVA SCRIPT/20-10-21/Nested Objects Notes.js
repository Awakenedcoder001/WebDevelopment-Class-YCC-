var playerDetail={
    name:"sachin Tendukor",
    age:40,
    matchs:{
        odi:20,
        test:100,
        t20:25
    }
}
//accessing the objects
console.log(playerDetail)
// accessing nested objects
console.log(playerDetail.matchs)
//accesing elements values of nested objects
console.log(playerDetail.matchs.test)
//accessing nested objects using squre brackets
console.log(playerDetail["matchs"])
// accessing elements of nested objects using squre brackets
console.log(playerDetail["matchs"]["test"])
// accessing elements of nested objects using combination of brackets and dot operaters
console.log(playerDetail["matchs"].test)
console.log(playerDetail.matchs["test"])