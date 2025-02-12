use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: u32 = next().parse().unwrap();
    let msb = 31 - n.leading_zeros();
    print!("{}", 10 + msb);
}
