use std::io::{read_to_string, stdin};
use std::fmt::Write;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next();
    let mut stdout = String::new();

    while let Some(x) = next() {
        let x: usize = x.parse::<usize>().unwrap() * 10000000;
        let n: usize = next().unwrap().parse().unwrap();
        let mut nums: Vec<usize> = (0..n).map(|_| next().unwrap().parse().unwrap()).collect();
        nums.sort();

        let mut left = 0;
        let mut right = n as i32 - 1;

        let mut have = false;
        while left < right {
            let tmp = nums[left as usize] + nums[right as usize];

            if tmp < x {
                left += 1;
            } else if tmp > x {
                right -= 1;
            } else {
                have = true;
                writeln!(stdout, "yes {} {}", nums[left as usize], nums[right as usize]).unwrap();
                break;
            }
        }
        if !have {
            writeln!(stdout, "danger").unwrap();
        }
    }

    print!("{stdout}");
}
