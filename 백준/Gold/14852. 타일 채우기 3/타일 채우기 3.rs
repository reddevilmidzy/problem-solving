use std::io;
use std::cmp::max;

const MOD: i64 = 1_000_000_007;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: usize = input.trim().parse().expect("Failed to parse");

    let mut dp = vec![[0; 2]; max(n + 1, 3)];

    dp[0][0] = 1;
    dp[1][0] = 2;
    dp[2][0] = 7;

    dp[1][1] = 2;
    dp[2][1] = dp[1][0] + dp[2][0];

    for i in 3..=n {
        dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 2][0] * 3 + dp[i - 3][1] * 2 + 2) % MOD;
        dp[i][1] = (dp[i-1][1] + dp[i][0]) % MOD;
    }
    print!("{}", dp[n][0]);
}