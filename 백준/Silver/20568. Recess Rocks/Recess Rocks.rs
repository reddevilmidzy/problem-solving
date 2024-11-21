use std::collections::HashSet;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();
    let n: usize = input.next().unwrap().unwrap().parse().unwrap();

    let nums: HashSet<i32> = input.next().unwrap().unwrap().split_whitespace().map(|s| s.parse().unwrap()).collect();

    print!("{}", n - nums.len())
}
