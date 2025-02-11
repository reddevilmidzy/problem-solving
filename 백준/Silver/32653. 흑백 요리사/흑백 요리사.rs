use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b > 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn lcm(a: u64, b: u64) -> u64 {
    (a * b) / gcd(a, b)
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: HashSet<u8> = (0..n)
        .map(|_| next().parse().unwrap())
        .map(|x: u8| x * 2)
        .collect();

    let mut a = 1;
    for num in nums {
        a = lcm(a, num as u64);
    }
    print!("{a}");
}
