use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let t: usize = next().parse().unwrap();
    let mut res = String::with_capacity(t);
    let dp = solve();

    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        writeln!(res, "{}", dp[n] + 1).unwrap();
    }
    print!("{res}");
}

fn gcd(a: i32, b: i32) -> i32 {
    if b == 0 {
        return a;
    }
    gcd(b, a % b)
}

fn solve() -> Vec<i32> {
    let n = 1000;
    let mut dp = vec![0; n + 1];
    for i in 1..=n {
        dp[i] = dp[i - 1];
        for j in 0..i {
            if gcd(i as i32, j as i32) == 1 {
                dp[i] += 2;
            }
        }
    }
    dp
}

#[test]
fn tmp() {
    solve();
}
