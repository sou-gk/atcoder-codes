function Main(input) {
  input = input.split("\n");
  tmp = input[1].split(" ");
  let a = parseInt(input[0], 10);
  let b = parseInt(tmp[0], 10);
  let c = parseInt(tmp[1], 10);
  let s = input[2];
  console.log('%d %s', a + b + c, s);
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
