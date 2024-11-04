const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const n = parseInt(input)
var dp = [0,];

for (var i = 0; i <= n; i++) {
    dp[i] = Infinity;
}
dp[3] = 1;
dp[5] = 1;

for (var i = 6; i <= n; i++) {
    if (dp[i-3] != Infinity) {
        dp[i] = Math.min(dp[i-3] + 1, dp[i]);
    }
    if (dp[i-5] != Infinity) {
        dp[i] = Math.min(dp[i-5] + 1, dp[i]);
    }
}
if (dp[n] == Infinity) {
    console.log(-1);
} else {
    console.log(dp[n]);
}
