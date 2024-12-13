use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut cant = HashSet::new();

    for i in 0..n {
        let diff = i as i32 - (nums[i] - 1);
        cant.insert((n as i32 + diff) % n as i32);
    }

    for i in 0..n {
        if !cant.contains(&(i as i32)) {
            print!("{i}");
            return;
        }
    }
    print!("-1")
}
