use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n = next().parse::<usize>().unwrap();
    let mut nums = (0..n)
        .map(|_| next().parse::<u32>().unwrap())
        .collect::<Vec<_>>();
    print!("{}", solve(n, &mut nums));
}

fn solve(n: usize, nums: &mut Vec<u32>) -> u32 {
    let mut res = 0;
    nums.sort_unstable();
    nums.reverse();

    for i in 1..=n {
        let mut ans = 0;

        for j in 0..i {
            if nums[j] > j as u32 {
                ans += nums[j] - j as u32;
            } else {
                break;
            }
        }

        res = res.max(ans);
    }

    res
}
