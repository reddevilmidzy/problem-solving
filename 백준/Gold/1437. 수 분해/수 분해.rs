use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: u32 = next().parse().unwrap();
    print!("{}", solve(n));
}

fn solve(n: u32) -> u32 {
    if n == 0 {
        return 0;
    } else if n == 1 {
        return 1;
    } else {
        let mut res = 1;
        for _ in 0..(n / 3 - if n % 3 == 1 { 1 } else { 0 }) {
            res *= 3;
            res %= 10007;
        }
        if n % 3 == 1 {
            res *= 4;
            res %= 10007;
        } else if n % 3 == 2 {
            res *= 2;
            res %= 10007;
        }
        return res;
    }
}
