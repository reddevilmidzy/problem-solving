use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<Vec<i32>> = (0..n).map(|_| (0..2).map(|_| next().parse::<i32>().unwrap()).collect()).collect();

    let mut dp: Vec<Vec<i32>> = vec![vec![i32::MAX; 2]; n];

    // dp[i][j] = i까지 진행했을 때, j=0이라면 아직 참가안할 수 있음, j=1 이전에 참가안한 대회가 있음
    // 때 최소값..?
    dp[0][0] = nums[0][1];
    dp[0][1] = 0;

    for i in 1..n {
        if dp[i - 1][0] <= nums[i][0] {
            dp[i][0] = dp[i - 1][0] + nums[i][1];
        }
        // 현재꺼 건너뛰기
        if dp[i - 1][0] != i32::MAX {
            dp[i][1] = dp[i - 1][0] + nums[i][1];
        }
        // 하나전거 건너뛰기
        if i > 1 && dp[i - 2][0] <= nums[i][0] {
            dp[i][1] = dp[i][1].min(dp[i - 2][0] + nums[i][1]);
        }
        if dp[i - 1][1] <= nums[i][0] {
            dp[i][1] = dp[i][1].min(dp[i - 1][1] + nums[i][1]);
        }
    }
    // println!("{:?}", dp);
    if dp[n - 1][0] != i32::MAX || dp[n - 1][1] != i32::MAX {
        print!("Kkeo-eok");
    } else {
        print!("Zzz");
    }
}
