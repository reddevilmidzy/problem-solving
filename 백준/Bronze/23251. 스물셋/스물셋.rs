use std::io::{read_to_string, stdin};
use std::fmt::Write;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();
    let mut stdout = String::new();

    let t: usize = next().parse().unwrap();

    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        writeln!(stdout, "{}", n * 23).unwrap();
    }
    print!("{stdout}");
}
