const input = require("fs").readFileSync("/dev/stdin", "utf8")
const [n, a, b] = input.split(" ").map(v => parseInt(v, 10))

let sum = 0

for (let value = 1; value <= n; value++) {

  const sp = value.toString().split("").map(v => parseInt(v, 10))

  const spsum = sp.reduce((acc, cur) => acc + cur, 0)

  if (spsum >= a && spsum <= b) {
    sum += value
  }

}

console.log(sum)
