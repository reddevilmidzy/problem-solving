use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let a: usize = next().parse().unwrap();
    let b: usize = next().parse().unwrap();

    let m: usize = next().parse().unwrap();
    let nums: Vec<usize> = (0..m).map(|_| next().parse().unwrap()).collect();
    let inf = 1_000_000_007;
    let mut dp: Vec<Vec<Vec<u32>>> = vec![vec![vec![inf; n + 1]; n + 1]; m + 1];


    dp[0][a][b] = 0;
    dp[0][b][a] = 0;

    for idx in 1..=m {
        for i in 0..=n {
            for j in 0..=n {
                if i == j {
                    continue;
                }
                let nxt = nums[idx-1];
                if nxt > n {
                    continue;
                }
                dp[idx][nxt][j] = dp[idx][nxt][j].min(dp[idx-1][i][j] + if i != 0 {nxt.abs_diff(i) as u32} else {a.abs_diff(i) as u32});
                dp[idx][i][nxt] = dp[idx][i][nxt].min(dp[idx-1][i][j] + if j != 0 {nxt.abs_diff(j) as u32} else {b.abs_diff(j) as u32});
            }
        }
    }
    let mut res = inf;
    for i in 1..=n {
        res = res.min(dp[m][nums[m-1]][i]);
    }
    print!("{res}");
}
