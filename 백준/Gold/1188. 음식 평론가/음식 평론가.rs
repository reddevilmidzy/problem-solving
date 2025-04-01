use std::io::{read_to_string, stdin};

fn gcd(mut a: u32, mut b: u32) -> u32 {
    while b != 0 {
        let tmp = b;
        b = a % b;
        a = tmp;
    }
    a
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let a: u32 = next().parse().unwrap();
    let b: u32 = next().parse().unwrap();

    print!("{}", b - gcd(a, b));
}
