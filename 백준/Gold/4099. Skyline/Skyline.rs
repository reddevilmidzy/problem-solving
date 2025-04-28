use std::io::{read_to_string, stdin};
use std::fmt::Write;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n = 1_000;
    let m = 1_000_000;

    let mut dp = vec![0u64; n + 1];
    dp[0] = 1;
    dp[1] = 1;

    for i in 1..=n {
        let mut tmp = 0;
        for j in 0..i {
            tmp = (tmp + dp[j] * dp[i - 1 - j]) % m;
        }
        dp[i] = tmp;
    }

    let mut stdout = String::new();
    loop {
        let x: usize = next().parse().unwrap();
        if x == 0 {
            break;
        }
        writeln!(stdout, "{}", dp[x]).unwrap();
    }
    print!("{stdout}");
}
