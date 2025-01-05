use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut stdout = String::new();

    let n: usize = next().parse().unwrap();
    for i in 0..n {
        write!(stdout, "{} ", 2 * i + 1).unwrap();
    }
    print!("{stdout}")
}
