function Main(input){
  const args = input.split('\n');
  const a = 4;
  const b = 3;
  let anwser = a * b;
  if (anwser % 2 == 0){
    console.log("Even")
  } else{
    consolel.log("Odd")
  }
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
