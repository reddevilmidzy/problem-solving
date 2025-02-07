use std::collections::VecDeque;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();

    print!("{}", solve(n, m, nums));
}

fn solve(n: usize, m: usize, nums: Vec<i32>) -> i64 {
    let mut res = i64::MIN;
    let mut dp: VecDeque<(i64, usize)> = VecDeque::new();

    for i in 0..n {
        while !dp.is_empty() && !(i - dp.front().unwrap().1 <= m) {
            dp.pop_front();
        }
        let val = if dp.is_empty() {
            nums[i] as i64
        } else {
            (nums[i] as i64).max(dp.front().unwrap().0 + nums[i] as i64)
        };
        while !dp.is_empty() && dp.back().unwrap().0 <= val {
            dp.pop_back();
        }
        res = res.max(val);
        dp.push_back((val, i));
    }

    res
}
