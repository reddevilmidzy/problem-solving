use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: u64 = next().parse().unwrap();
    let mut dp = vec![0u64; n / 2 + 1];
    dp[0] = 1;
    dp[1] = 1;

    for i in 1..=n/2 {
        let mut tmp = 0u64;
        for j in 0..i {
            tmp = (tmp + (dp[j] * dp[i - j]) % m) % m;
        }
        dp[i] = tmp;
    }

    print!("{}", dp[n / 2]);
}
