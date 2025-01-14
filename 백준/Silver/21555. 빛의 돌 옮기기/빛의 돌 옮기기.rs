use std::cmp::min;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();
    let k: u64 = next().parse().unwrap();

    let a: Vec<u64> = (0..n).map(|_| next().parse().unwrap()).collect();
    let b: Vec<u64> = (0..n).map(|_| next().parse().unwrap()).collect();

    // dp[i][j] = j방법으로 i 번 돌까지 옮김.
    // j=0 끌고감, j=1 들고감
    let mut dp: Vec<Vec<u64>> = vec![vec![u64::MAX; 2]; n];

    dp[0][0] = a[0];
    dp[0][1] = b[0];

    for i in 1..n {
        dp[i][0] = min(dp[i - 1][0] + a[i], dp[i - 1][1] + k + a[i]);
        dp[i][1] = min(dp[i - 1][1] + b[i], dp[i - 1][0] + k + b[i])
    }

    print!("{}", dp[n - 1][0].min(dp[n - 1][1]))
}
