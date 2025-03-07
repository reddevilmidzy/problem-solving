use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let inf = 2_000_000_007;
    let mut dp = vec![vec![inf; n + 1]; n + 1];

    dp[0][0] = 0;

    for i in 0..=n {
        for j in 0..=n {
            let nxt = i.max(j) + 1;
            if nxt > n {
                continue;
            }
            dp[nxt][j] = dp[nxt][j].min(
                dp[i][j]
                    + if i != 0 {
                        nums[i - 1].abs_diff(nums[nxt - 1])
                    } else {
                        0
                    },
            );
            dp[i][nxt] = dp[i][nxt].min(
                dp[i][j]
                    + if j != 0 {
                        nums[j - 1].abs_diff(nums[nxt - 1])
                    } else {
                        0
                    },
            );
        }
    }

    let mut res = inf;
    for i in 0..=n {
        res = res.min(dp[n][i]);
    }
    print!("{res}");
}
