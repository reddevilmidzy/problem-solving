use std::cmp::min;
use std::io::{self, BufRead};

const INF: i32 = i32::MAX;

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let first_line = input.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let mut nums: Vec<Vec<i32>> = Vec::with_capacity(n);
    for _ in 0..n {
        let line = input.next().unwrap().unwrap();
        let row: Vec<i32> = line.split_whitespace().map(|x| x.parse().unwrap()).collect();
        nums.push(row);
    }

    // dp[i][j][k] nums[i][j] 에서 왼중우
    let mut dp: Vec<Vec<[i32; 3]>> = vec![vec![[INF; 3]; m]; n];

    for j in 0..m {
        dp[0][j] = [nums[0][j]; 3];
    }

    for i in 1..n {
        for j in 0..m {
            if j != 0 {
                dp[i][j][2] = nums[i][j] + min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]);
            }
            if j != m - 1 {
                dp[i][j][0] = nums[i][j] + min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]);
            }
            dp[i][j][1] = nums[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2]);
        }
    }

    let res = dp[n - 1].iter().flat_map(|row| row.iter().cloned()).min().unwrap();
    print!("{}", res);
}
