const input = require("fs").readFileSync("/dev/stdin", "utf8")
const [, tmp] = input.split("\n")
const a = tmp.split(" ").map(v => parseInt(v, 10))

const score = {
  "Alice": 0,
  "Bob": 0,
}

const cards = a.sort((a, b) => b - a)

for (const [index, card] of cards.entries()) {

  const player = (index & 1) ? "Bob" : "Alice"
  score[player] += card

}

const answer = score["Alice"] - score["Bob"]
console.log(answer)
