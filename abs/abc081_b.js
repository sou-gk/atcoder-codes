const input = require("fs").readFileSync("/dev/stdin", "utf8")
const [n, tmp] = input.split("\n")
const a = tmp.split(" ").map(v => parseInt(v, 10))

let count = Number.POSITIVE_INFINITY

for (let c of a) {

  c ^= c - 1
  c >>>= 1

  c = (c >>> 1 & 0x55555555) + ((c & 0x55555555) >>> 0)
  c = (c >>> 2 & 0x33333333) + ((c & 0x33333333) >>> 0)
  c = (c >>> 4 & 0x0F0F0F0F) + ((c & 0x0F0F0F0F) >>> 0)
  c = (c >>> 8 & 0x00FF00FF) + ((c & 0x00FF00FF) >>> 0)
  c = (c >>> 16 & 0x0000FFFF) + ((c & 0x0000FFFF) >>> 0)

  if (count > c) {
    count = c
  }

}

console.log(count)
