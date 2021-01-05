const fs = require("fs");
const Table = require("cli-table");

let string;

fs.readFile("Titanic.csv", "utf8", (err, data) => {
  if (err) return console.error(err);
  string = data.toString().split("\n").map(function(data){
    return data.match(/(".*?"(?=,)|[^",]+)/g);

  });
  string.pop();

  function result(key, Name, Pclass, Age, Sex, Survived, SexCode) {
    return {
      key: key.slice(1, key.length - 1),
      name: Name.slice(1, Name.length - 1),
      Pclass: Pclass.slice(1, Pclass.length - 1),
      Age: Age,
      Sex: Sex.slice(1, Sex.length - 1),
      Survived: Survived,
      SexCode: SexCode
    }
  }
  let array = [];
  for (var index = 0; index < string.length; index++) {
    array.push(result(string[index][0], string[index][1], string[index][2], string[index][3], string[index][4], string[index][5], string[index][6]));
    array.forEach(function(record){
        if (Object.values(record)[2] === "1st") {
          counter1++;
        } else if (Object.values(record)[2] === "2nd") {
          counter2++;
        } else {
          counter3++;
        }
      });    
    let counter1 = 0;
    let counter2 = 0;
    let counter3 = 0;
    let arrayData1;
    let arrayData2;
    let arrayData3;
    arrayData1 = ["1st", counter1]; 
    arrayData2 = ["2nd", counter2];
    arrayData3 = ["3rd", counter3];
    const table = new Table({
      chars: {
        top: "═", "top-mid": "╤", "top-left": "╔", "top-right": "╗", bottom: "═",
        "bottom-mid": "╧", "bottom-left": "╚", "bottom-right": "╝",
        left: "║", "left-mid": "╟", mid: "─", "mid-mid": "┼",
        right: "║", "right-mid": "╢", middle: "│" },
      head: ["PClass", "TotalCount"],
     });
    table.push(
       arrayData1, arrayData2, arrayData3
     );
    console.log(table.toString());
     };