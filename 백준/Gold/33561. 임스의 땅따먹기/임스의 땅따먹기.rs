use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<Vec<i32>> = (0..n)
        .map(|_| (0..n).map(|_| next().parse().unwrap()).collect())
        .collect();

    let k: usize = next().parse().unwrap();
    let mut d: Vec<i32> = (0..k).map(|_| next().parse().unwrap()).collect();
    d.sort();
    d.reverse();

    let mut d_pre = vec![0; k + 1];

    for i in 1..=k {
        d_pre[i] = d_pre[i - 1] + d[i - 1];
    }

    let k = k as i32;

    let mut no_build = vec![vec![0i32; n + 1]; n + 1];
    let mut pre = vec![vec![0; n + 1]; n + 1];

    for i in 1..=n {
        for j in 1..=n {
            let cur: i32 = if nums[i - 1][j - 1] > 0 { 0 } else { 1 };
            no_build[i][j] = no_build[i - 1][j] + no_build[i][j - 1] + cur - no_build[i - 1][j - 1];
            pre[i][j] = pre[i - 1][j] + pre[i][j - 1] + nums[i - 1][j - 1] - pre[i - 1][j - 1];
        }
    }

    let mut res = 0;
    for size in 1..=n {
        for i in 0..=n - size {
            for j in 0..=n - size {
                let no_cnt =
                    no_build[i + size][j + size] - no_build[i][j + size] - no_build[i + size][j]
                        + no_build[i][j];
                let build =
                    pre[i + size][j + size] - pre[i][j + size] - pre[i + size][j] + pre[i][j];

                if no_cnt > k {
                    continue;
                }
                let cur = build + d_pre[no_cnt as usize];
                res = res.max(cur);
            }
        }
    }
    print!("{res}");
}
