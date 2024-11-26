use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let k: usize = next().parse().unwrap();
    let nums: Vec<Vec<i32>> = (0..n).map(|_| (0..m).map(|_| next().parse().unwrap()).collect()).collect();

    let mut pre: Vec<Vec<i32>> = vec![vec![0; m + 1]; n + 1];

    for i in 1..=n {
        for j in 1..=m {
            pre[i][j] = pre[i - 1][j] + pre[i][j - 1] + nums[i - 1][j - 1] - pre[i - 1][j - 1];
        }
    }
    let mut res = 0;

    for i in 1 + k..=n - k {
        for j in 1 + k..=m - k {
            let weight = pre[i][j + k] - pre[i][j - k - 1] - pre[i - 1][j + k] + pre[i - 1][j - k - 1];
            let height = pre[i + k][j] - pre[i - k - 1][j] - pre[i + k][j - 1] + pre[i - k - 1][j - 1];
            if weight == height && weight == k as i32 * 2 + 1 {
                res += 1;
            }
        }
    }

    print!("{res}")
}
