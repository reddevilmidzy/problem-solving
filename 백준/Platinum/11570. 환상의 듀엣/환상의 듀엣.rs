use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut nums: Vec<u32> = vec![0; n + 2];
    for i in 1..=n {
        nums[i] = next().parse().unwrap();
    }

    print!("{}", solve(n, nums));
}

fn solve(n: usize, nums: Vec<u32>) -> u32 {
    let inf = 10u32.pow(9);
    let mut dp = vec![vec![inf; n + 2]; n + 2];

    dp[0][0] = 0;
    dp[1][0] = 0;
    dp[0][1] = 0;

    for i in 0..=n {
        for j in 0..=n {
            if i == j {
                continue;
            } else {
                let nxt = i.max(j) + 1;
                dp[nxt][j] = dp[nxt][j].min(dp[i][j] + if i != 0 {nums[i].abs_diff(nums[nxt])} else {0});
                dp[i][nxt] = dp[i][nxt].min(dp[i][j] + if j != 0 {nums[j].abs_diff(nums[nxt])} else {0});
            }
        }
    }

    let mut res = inf;
    for i in 0..=n {
        res = res.min(dp[n][i]);
    }
    res
}
