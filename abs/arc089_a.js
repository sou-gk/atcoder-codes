const input = require("fs").readFileSync("/dev/stdin", "utf8")
const [N, ...temp] = input.split("\n")

temp.pop()

const plans = temp.map(line => {
  const args = line.split(" ").map(v => parseInt(v, 10))
  return {
    t: args[0],
    x: args[1],
    y: args[2],
  }
})

const start = { t: 0, x: 0, y: 0, }

for (const [index, plan] of plans.entries()) {

  const prev = index == 0 ? start : plans[index - 1]
  const time = plan.t - prev.t
  const distance = Math.abs(plan.x - prev.x) + Math.abs(plan.y - prev.y)

  const def = time - distance

  if ((distance > time) || (def & 1)) {
    console.log("No")
    return
  }

}

console.log("Yes")
