//Q1: Bob argues that Marley's statement is not a string. Prove Bob wrong!

let Marley= 'I am a Rasta Man';
console.log(typeof Marley);

//Q2: Dom wanted his text to be reversed so that he could print it and add it from within the window of a car. Convert the text into reverse form?
const word = "Fast And Furious Rocks";
const reversedWord = [...word].reverse().join("");
console.log(reversedWord);

//Q3: Tony Chopper wants to search a particular word from the text. Show him how to do it...?
let str = "One piece is the Greatest anime ever";
console.log(str.search("anime"))
console.log(str);

//Q4:How does great man Laugh 
const laughing = "ra".repeat(4);
console.log("Za",laughing);

//Q5: Robin wants to encrypt her last three password showing only her first three password. How to do it using JS?
const anonymizedCode = "999".padEnd(6, "*");
console.log(anonymizedCode);
/*const eightBitss = "001".padStart(8, "0");
console.log(eightBitss); // "00000001"*/ //for adding characters at the begining

//Q6: Split the Word 'Kozuki Momonosuke'
const wordd = "Kozuki Momonosuke";
const characters = [...wordd];
console.log(characters);

//Q7: Help Ussop replace the 'run away' with 'Fight back'
const text = "Since early in the series, he has struggled to match the physical feats of the stronger characters, and needed his weapons or ammunition to take out foes. He used to be a huge coward and often wanted to run away immediately, a trait he still carries to a lesser extent after his two years of training. This, coupled with him getting easily distracted or confused in battle have often made him less effective than his real potential as a sniper."

console.log(text.replace(/run away/g, "fight back"));//'g' is for all


