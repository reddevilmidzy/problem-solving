use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn gcd(a: u32, b: u32) -> u32 {
    if b == 0 {
        return a;
    }
    gcd(b, a % b)
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut res = String::new();

    let t: u32 = next().parse().unwrap();
    for _ in 0..t {
        let (u, v, w): (u32, u32, u32) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );
        writeln!(res, "{}", solve(u, v, w)).unwrap();
    }

    print!("{res}");
}

fn solve(u: u32, v: u32, w: u32) -> String {
    if w % gcd(u, v) == 0 {
        return "Yes".to_string();
    }
    "No".to_string()
}
