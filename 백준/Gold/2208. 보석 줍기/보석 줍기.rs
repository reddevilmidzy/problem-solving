use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let mut nums: Vec<i32> = vec![0; n + 1];
    for i in 1..=n {
        nums[i] = next().parse().unwrap();
        nums[i] += nums[i-1];
    }
    print!("{}", solve(n, m, nums));
}

fn solve(n: usize, m: usize, nums: Vec<i32>) -> i32 {

    let mut res = 0;
    let mut cur = 0;
    for i in m..=n {
        cur = cur.min(nums[i - m]);
        res = res.max(nums[i] - cur);
    }

    res
}
