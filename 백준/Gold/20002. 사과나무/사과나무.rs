use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let board: Vec<Vec<i32>> = (0..n)
        .map(|_| (0..n).map(|_| next().parse::<i32>().unwrap()).collect())
        .collect();

    let mut pre = vec![vec![0; n + 1]; n + 1];

    for i in 1..=n {
        for j in 1..=n {
            pre[i][j] = pre[i - 1][j] + pre[i][j - 1] + board[i - 1][j - 1] - pre[i - 1][j - 1];
        }
    }

    let mut res = i32::MIN;

    for k in 0..n {
        for i in 1..=n-k {
            for j in 1..=n-k {
                let tmp =
                    pre[i + k][j + k] - pre[i - 1][j + k] - pre[i + k][j - 1] + pre[i - 1][j - 1];
                res = res.max(tmp);
            }
        }
    }
    print!("{res}");
}
