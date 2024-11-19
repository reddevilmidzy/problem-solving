use std::io::{self, BufRead};

const POINT: [[i32; 2]; 13] = [[-1, -1],
    [0, 0], [0, 1], [0, 2],
    [1, 0], [1, 1], [1, 2],
    [2, 0], [2, 1], [2, 2],
    [3, 0], [3, 1], [3, 2]];

fn cal_dist(st: usize, ed: usize) -> i32 {
    (POINT[st][0] - POINT[ed][0]).abs() + (POINT[st][1] - POINT[ed][1]).abs()
}

fn solve(dp: &mut Vec<Vec<Vec<i32>>>, nums: &Vec<i32>, idx: usize, cur_a: usize, cur_b: usize, val_a: i32, val_b: i32) -> i32 {
    if idx == nums.len() {
        return 0;
    }

    if dp[idx][cur_a][cur_b] != -1 {
        return dp[idx][cur_a][cur_b];
    }

    let nxt_num = nums[idx] as usize;

    let a_move = cal_dist(cur_a, nxt_num) + val_a;
    let b_move = cal_dist(cur_b, nxt_num) + val_b;

    let res = (solve(dp, nums, idx + 1, nxt_num, cur_b, val_a, val_b) + a_move)
            .min(solve(dp, nums, idx + 1, cur_a, nxt_num, val_a, val_b) + b_move);

    dp[idx][cur_a][cur_b] = res;
    dp[idx][cur_a][cur_b]
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let first_line = input.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();
    let a: i32 = iter.next().unwrap().parse().unwrap();
    let b: i32 = iter.next().unwrap().parse().unwrap();

    let nums: Vec<i32> = input.next().unwrap().unwrap().split_whitespace().map(|s| s.parse().unwrap()).collect();

    let mut dp: Vec<Vec<Vec<i32>>> = vec![vec![vec![-1; 13]; 13]; n];

    // 왼손 엄지 a
    // 오른손 엄지 b
    print!("{}", solve(&mut dp, &nums, 0, 1, 3, a, b));
}
