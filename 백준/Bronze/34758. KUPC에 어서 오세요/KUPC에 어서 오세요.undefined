use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let (x, y): (i32, i32) = (next().parse().unwrap(), next().parse().unwrap());
    let n: usize = next().parse().unwrap();
    let mut res = String::with_capacity(n);

    for _ in 0..n {
        let (r, c): (i32, i32) = (next().parse().unwrap(), next().parse().unwrap());
        writeln!(res, "{}", if r == x || c == y { 0 } else { 1 }).unwrap();
    }
    print!("{res}");
}
