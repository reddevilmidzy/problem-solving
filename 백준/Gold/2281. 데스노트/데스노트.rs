use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let first_line = input.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: i32 = iter.next().unwrap().parse().unwrap();

    let mut nums = Vec::with_capacity(n);
    for _ in 0..n {
        let num: i32 = input.next().unwrap().unwrap().trim().parse().unwrap();
        nums.push(num);
    }

    let mut dp = vec![i32::MAX; n + 1];
    dp[0] = 0;

    for i in 1..=n {
        let mut cur = 0;
        for j in (0..i).rev() {
            cur += nums[j];
            if cur + (i - j - 1) as i32 > m {
                break;
            }
            let cost = if i == n {
                0
            } else {
                (m - cur - (i - j - 1) as i32).pow(2)
            };
            dp[i] = dp[i].min(dp[j] + cost);
        }
    }

    print!("{}", dp[n]);
}
