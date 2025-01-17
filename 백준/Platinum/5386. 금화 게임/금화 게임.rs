use std::collections::HashSet;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn solve(s: u32, k: u32) -> u32 {
    if k % 2 != 0 {
        return s % 2;
    }
    let s = s % (k + 1);
    if s == k {
        return k;
    }
    s % 2
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut stdout = String::new();

    let t: usize = next().parse().unwrap();
    for _ in 0..t {
        let s: u32 = next().parse().unwrap();
        let k: u32 = next().parse().unwrap();

        writeln!(stdout, "{}", solve(s, k)).unwrap();
    }
    print!("{stdout}")
}
