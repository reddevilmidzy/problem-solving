use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let t: usize = next().parse().unwrap();
    let mut res = String::with_capacity(t);

    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();

        writeln!(res, "{}", solve(n, nums)).unwrap();
    }
    print!("{}", res);
}

fn solve(n: usize, nums: Vec<u32>) -> usize {
    n
}
