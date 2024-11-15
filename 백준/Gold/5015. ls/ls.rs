use std::io::{self, BufRead};

fn solve(dp: &mut Vec<Vec<i8>>, p: &str, s: &str, p_idx: usize, s_idx: usize) -> i8 {
    if dp[p_idx][s_idx] != -1 {
        return dp[p_idx][s_idx];
    }

    if p_idx < p.len() && s_idx < s.len() && p.as_bytes()[p_idx] == s.as_bytes()[s_idx] {
        dp[p_idx][s_idx] = solve(dp, p, s, p_idx + 1, s_idx + 1);
        return dp[p_idx][s_idx];
    }

    if p_idx == p.len() {
        dp[p_idx][s_idx] = if s_idx == s.len() { 1 } else { 0 };
        return dp[p_idx][s_idx];
    }

    if p.as_bytes()[p_idx] == b'*' {
        if solve(dp, p, s, p_idx + 1, s_idx) == 1 || (s_idx < s.len() && solve(dp, p, s, p_idx, s_idx + 1) == 1) {
            dp[p_idx][s_idx] = 1;
            return dp[p_idx][s_idx];
        }
    }

    dp[p_idx][s_idx] = 0;
    dp[p_idx][s_idx]
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let p = input.next().unwrap().unwrap();
    let n: usize = input.next().unwrap().unwrap().parse().unwrap();
    let m = 100;
    let mut res = Vec::new();

    for _ in 0..n {
        let mut dp = vec![vec![-1; m + 1]; m + 1];
        let s = input.next().unwrap().unwrap();
        if solve(&mut dp, &p, &s, 0, 0) == 1 {
            res.push(s);
        }
    }

    for r in res {
        println!("{}", r);
    }
}