use std::{
    fmt::Write,
    io::{read_to_string, stdin},
};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let t: usize = next().parse().unwrap();
    let mut res = String::with_capacity(t);
    const MOD: u64 = 1_000_000_009;
    let m = 100_000;
    let mut dp = vec![0; m + 1];

    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 2;
    dp[4] = 3;
    dp[5] = 3;

    for i in 6..=m {
        dp[i] = dp[i - 2] + dp[i - 4] + dp[i - 6];
        dp[i] %= MOD;
    }
    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        writeln!(res, "{}", dp[n]).unwrap();
    }
    print!("{res}");
}
