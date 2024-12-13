use std::io::{read_to_string, stdin};

fn lower_bound(nums: &Vec<usize>, k: usize) -> usize {
    let mut left: i32 = 0;
    let mut right: i32 = nums.len() as i32 - 1;

    while left <= right {
        let mid = (left + right) / 2;
        if nums[mid as usize] < k {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    left as usize
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut dp = Vec::new();
    
    for num in &nums {
        let k = lower_bound(&dp, *num);
        if dp.len() <= k {
            dp.push(*num);
        } else {
            dp[k] = *num;
        }
    }
    print!("{}", dp.len());
}
