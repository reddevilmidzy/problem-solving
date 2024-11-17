use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();
    let n: usize = input.next().unwrap().unwrap().parse().unwrap();
    let mut nums: Vec<i64> = input.next().unwrap().unwrap().split_whitespace().map(|s| s.parse().unwrap()).collect();
    nums.sort();
    let mut res = nums[n - 1];
    let m = n - n % 2;
    for i in 0..m {
        res = res.max(nums[m - i - 1] + nums[i]);
    }
    print!("{res}")
}
