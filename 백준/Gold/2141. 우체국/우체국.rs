use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut nums: Vec<(i64, u32)> = (0..n)
        .map(|_| (next().parse().unwrap(), next().parse().unwrap()))
        .collect();
    nums.sort_unstable();

    print!("{}", solve(n, nums));
}

fn solve(n: usize, nums: Vec<(i64, u32)>) -> i64 {
    let mut tot = 0;
    for i in 0..n {
        tot += nums[i].1 as u64;
    }
    tot = (tot + 1) / 2;
    let mut cur = 0;
    for i in 0..n {
        cur += nums[i].1 as u64;

        if cur >= tot {
            return nums[i].0;
        }
    }
    unreachable!()
}
