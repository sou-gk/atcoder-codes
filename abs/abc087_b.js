const input = require("fs").readFileSync("/dev/stdin", "utf8")
const [a, b, c, x] = input.split("\n").map(v => parseInt(v, 10))

let count = 0;
for (let i = 0; i <= a; i++) {
  for (let j = 0; j <= b; j++) {
    for (let k = 0; k <= c; k++) {
      if (((500 * i) + (100 * j) + (50 * k)) === x) {
        count++
      }
    }
  }
}

console.log(count)
