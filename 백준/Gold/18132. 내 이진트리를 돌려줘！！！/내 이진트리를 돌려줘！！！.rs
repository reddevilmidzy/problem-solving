use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut res = String::new();

    let n: usize = 5_002;
    const MOD: u64 = 1_000_000_007;
    let mut dp = vec![0u64; n + 1];
    dp[0] = 1;
    dp[1] = 1;

    let t: usize = next().parse().unwrap();

    for i in 1..=n {
        let mut tmp = 0u64;
        for j in 0..i {
            tmp = ((tmp % MOD) + (dp[j] * dp[i - j]) % MOD) % MOD;
        }
        dp[i] = tmp;
    }

    for _ in 0..t {
        let e: usize = next().parse().unwrap();
        writeln!(res, "{}", dp[e + 2]).unwrap();
    }

    print!("{res}");
}
