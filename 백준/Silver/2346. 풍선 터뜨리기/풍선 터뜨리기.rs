use std::collections::VecDeque;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut res = String::new();

    let n: usize = next().parse().unwrap();
    let mut nums: VecDeque<(i32, usize)> =
        (0..n).map(|i| (next().parse().unwrap(), i + 1)).collect();

    for _ in 0..n {
        let (num, idx) = nums.pop_front().unwrap();
        write!(res, "{idx} ").unwrap();

        if nums.is_empty() {
            break;
        }
        if num > 0 {
            nums.rotate_left((num.abs() as usize - 1) % nums.len());
        } else {
            nums.rotate_right((num.abs() as usize) % nums.len());
        }
    }

    print!("{res}");
}
