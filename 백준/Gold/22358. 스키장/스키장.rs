use std::io::{read_to_string, stdin};

const INF: i64 = -1_000_000_000;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();
    let s: usize = next().parse().unwrap();
    let t: usize = next().parse().unwrap();

    let nums: Vec<(usize, usize, i64)> = (0..m).map(|_| (next().parse().unwrap(), next().parse().unwrap(), next().parse().unwrap())).collect();

    // dp[i][j] => i번 리프트 탑승했을 때, j번 지점에 있었을 때 스키탄 최대 시간

    let mut go = vec![Vec::new(); n + 1];
    let mut back = vec![Vec::new(); n + 1];

    for (u, v, w) in nums {
        go[u].push((v, w));
        back[v].push(u);
    }

    let mut dp = vec![vec![INF; n + 1]; k + 1];

    dp[0][t] = 0;

    for i in 0..=k {
        for j in (1..=n).rev() {
            for (u, w) in &go[j] {
                if dp[i][*u] == INF {
                    continue;
                }
                dp[i][j] = dp[i][j].max(dp[i][*u] + w);
            }

            if i > 0 {
                for v in &back[j] {
                    dp[i][j] = dp[i][j].max(dp[i - 1][*v]);
                }
            }
        }
    }
    let res = if dp[k][s] != INF {
        dp[k][s]
    } else {
        -1
    };
    print!("{res}")
}
