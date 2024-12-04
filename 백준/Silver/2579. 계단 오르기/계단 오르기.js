let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
// "/dev/stdin"
// "test/Test.txt"
const n = Number(input[0]);
const scores = [];
for (let i = 1; i <= n; i++) {
  scores.push(Number(input[i]));
}

const f = [
  scores[0],
  Math.max(scores[0], scores[0] + scores[1]),
  Math.max(scores[0] + scores[2], scores[1] + scores[2]),
];

for (let i = 3; i < n; i++) {
  let max = Math.max(
    f[i - 3] + scores[i - 1] + scores[i],
    f[i - 2] + scores[i]
  );

  f[i] = max;
}
console.log(f[n - 1]);