use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();
    let mut nums: Vec<u32> = (0..n * 3).map(|_| next().parse().unwrap()).collect();
    nums.sort();
    print!("{}", nums[n]);
}
