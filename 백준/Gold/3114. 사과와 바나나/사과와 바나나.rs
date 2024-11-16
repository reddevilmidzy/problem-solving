use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let first_line = input.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let mut a: Vec<Vec<i32>> = vec![vec![0; m + 1]; n + 1];
    let mut b: Vec<Vec<i32>> = vec![vec![0; m + 1]; n + 1];

    let mut dp: Vec<Vec<i32>> = vec![vec![0; m + 1]; n + 1];

    for i in 1..=n {
        let line = input.next().unwrap().unwrap();
        let mut iter = line.split_whitespace();
        for j in 1..=m {
            let cell = iter.next().unwrap();
            let c = cell.chars().next().unwrap();
            let val: i32 = cell[1..].parse().unwrap();

            if c == 'A' {
                a[i][j] = val;
            } else {
                b[i][j] = val;
            }
        }
    }

    for i in 1..=n {
        for j in 1..=m {
            a[i][j] += a[i][j - 1];
            b[i][j] += b[i][j - 1];
        }
    }

    for i in 1..=n {
        for j in 1..=m {
            a[i][j] += a[i - 1][j];
            b[i][j] += b[i - 1][j];
        }
    }

    for j in 1..=m {
        dp[1][j] = a[n][j] - a[1][j];
    }

    for i in 1..=n {
        dp[i][1] = a[n][1] - a[i][1];
    }

    for i in 2..=n {
        for j in 2..=m {

            //왼쪽
            dp[i][j] = dp[i][j].max(dp[i][j - 1] + b[i - 1][j] - b[i - 1][j - 1] - b[0][j] + b[0][j - 1]
                + a[n][j] - a[n][j - 1] - a[i][j] + a[i][j - 1]);

            // 아래로

            dp[i][j] = dp[i][j].max(dp[i - 1][j]
                - (a[i][j] - a[i][j - 1] - a[i - 1][j] + a[i - 1][j - 1]));

            // 대각
            dp[i][j] = dp[i][j].max(dp[i - 1][j - 1] + b[i - 1][j] - b[i - 1][j - 1] - b[0][j] + b[0][j - 1]
                + a[n][j] - a[n][j - 1] - a[i][j] + a[i][j - 1]);
        }
    }

    print!("{}", dp[n][m]);
}