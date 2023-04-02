const input = require("fs").readFileSync("/dev/stdin", "utf8")
const [S] = input.split("\n")

const answer = S.match(/^(dream|dreamer|erase|eraser)*$/) ? "YES" : "NO"
console.log(answer)
