use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: i32 = next().parse().unwrap();
    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut cant = HashSet::new();

    for i in 0..n {
        let diff = i - (nums[i as usize] - 1);
        cant.insert((n + diff) % n);
    }

    for i in 0..n {
        if !cant.contains(&i) {
            print!("{i}");
            return;
        }
    }
    print!("-1")
}
