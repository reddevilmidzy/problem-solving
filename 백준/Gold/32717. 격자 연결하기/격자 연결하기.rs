use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let nums: Vec<Vec<i32>> = (0..n).map(|_| (0..m).map(|_| next().parse::<i32>().unwrap()).collect()).collect();

    let mut lr: Vec<Vec<i32>> = vec![vec![-1_000_000; m + 1]; n + 1];
    let mut rl: Vec<Vec<i32>> = vec![vec![-1_000_000; m + 1]; n + 1];

    for i in 1..=n {
        for j in 1..=m {
            lr[i][j] = nums[i - 1][j - 1].max(lr[i - 1][j] + nums[i - 1][j - 1]).max(lr[i][j - 1] + nums[i - 1][j - 1])
        }
    }

    for i in 1..=n {
        for j in (0..m).rev() {
            rl[i][j] = nums[i - 1][j].max(rl[i][j + 1] + nums[i - 1][j]).max(rl[i - 1][j] + nums[i - 1][j])
        }
    }

    let mut res = -1_000_000;
    for i in 0..=n {
        for j in 0..=m {
            res = res.max(lr[i][j]).max(rl[i][j])
        }
    }
    print!("{res}");
}
