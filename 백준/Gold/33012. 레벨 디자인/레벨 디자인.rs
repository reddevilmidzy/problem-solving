use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();
    let mut stdout = String::new();

    let n: usize = next().parse().unwrap();

    let mut nums: Vec<usize> = vec![0; n];
    let mut left = 0;
    let mut right = n - 1;
    for i in 0..n {
        if i % 2 == 0 {
            nums[left] = i + 1;
            left += 1;
        } else {
            nums[right] = i + 1;
            right -= 1;
        }
    }

    let mut dp: Vec<usize> = vec![0; n];

    dp[0] = nums[0];
    if n > 1 {
        dp[1] = dp[0].max(nums[1]);
    }

    for i in 2..n {
        dp[i] = dp[i - 1].max(dp[i - 2] + nums[i]);
    }

    for num in nums {
        write!(stdout, "{num} ").unwrap();
    }
    writeln!(stdout, "").unwrap();
    writeln!(stdout, "{}", dp[n - 1]).unwrap();
    print!("{stdout}");
}
