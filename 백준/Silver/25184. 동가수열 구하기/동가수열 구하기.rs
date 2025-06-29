use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: u32 = next().parse().unwrap();
    let mut res = String::new();

    let mid = n / 2;
    for i in 1..=mid {
        write!(res, "{} {} ", i + mid, i).unwrap();
    }
    if n % 2 == 1 {
        write!(res, "{}", n).unwrap();
    }

    print!("{}", res);
}
