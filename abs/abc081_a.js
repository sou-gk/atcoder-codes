function Main(input){
  const args = input.split('\n');
  let x = 1;
  let y = 0;
  let z = 1;
  let i = 0;
  if (x == 1){
    i++ 
  } 
  if (y == 1){
    i++ 
  } 
  if (z == 1){
    i++ 
  } 
  console.log(i)
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
