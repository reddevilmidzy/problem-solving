use std::io::{read_to_string, stdin};
use std::fmt::Write;

fn lower_bound(nums: &Vec<usize>, target: usize) -> usize {
    let mut lo = 0;
    let mut hi = nums.len() as i32 - 1;

    while lo <= hi {
        let mid = (lo + hi) / 2;
        if nums[mid as usize] < target {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }

    lo as usize
}

fn solve(nums: Vec<usize>) -> usize {
    let mut dp: Vec<usize> = Vec::new();

    for num in nums {
        let k = lower_bound(&dp, num);
        if dp.len() <= k {
            dp.push(num);
        } else {
            dp[k] = num;
        }
    }

    dp.len()
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next();

    let mut stdout = String::new();

    while let Some(n) = next() {
        let n: usize = n.parse().unwrap();
        let nums: Vec<usize> = (0..n).map(|_| next().unwrap().parse().unwrap()).collect();
        writeln!(stdout, "{}", solve(nums)).unwrap();
    }

    print!("{stdout}")
}
