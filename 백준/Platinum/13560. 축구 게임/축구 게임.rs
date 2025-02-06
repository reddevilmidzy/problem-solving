use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(n, nums));
}

fn solve(n: usize, mut nums: Vec<u32>) -> i8 {
    let mut tot = 0;
    nums.sort();
    let mut left = 0;
    for i in (0..n).rev() {
        tot += nums[i];
        if nums[i] > left + i as u32 {
            return -1;
        }
        left = left + i as u32 - nums[i];
    }
    if tot != ((n - 1) * n / 2) as u32 {
        return -1;
    }

    1
}
