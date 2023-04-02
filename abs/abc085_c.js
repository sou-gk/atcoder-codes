const input = require("fs").readFileSync("/dev/stdin", "utf8")
const [N, Y] = input.split(" ").map(v => parseInt(v, 10))

for (let x = 0; x <= N; x++) {
  for (let y = 0; y <= N - x; y++) {
    const z = N - x - y
    if ((x * 10000) + (y * 5000) + (z * 1000) === Y) {
      console.log(`${x} ${y} ${z}`)
      return
    }
  }
}

console.log("-1 -1 -1")
