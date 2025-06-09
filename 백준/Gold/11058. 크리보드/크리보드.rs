use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut dp = vec![0u64; n.max(4) + 1];

    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;
    dp[4] = 4;

    for i in 5..=n {
        dp[i] = dp[i].max(dp[i - 1] + 1);
        dp[i] = dp[i].max(dp[i - 3] * 2);
        dp[i] = dp[i].max(dp[i - 4] * 3);
        dp[i] = dp[i].max(dp[i - 5] * 4);
    }

    print!("{}", dp[n]);
}
