use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut stdout = String::new();

    let q: usize = next().parse().unwrap();
    for _ in 0..q {
        let (x, y): (i64, i64) = (next().parse().unwrap(), next().parse().unwrap());

        // 가만이
        if x == 0 && y == 0 {
            writeln!(stdout, "0").unwrap();
        } else if y == 0 && x >= 0 {
            writeln!(stdout, "0").unwrap();
        } else if x >= 0 {
            writeln!(stdout, "1").unwrap();
        } else if x == 0 && y >= 0 {
            writeln!(stdout, "1").unwrap();
        } else if x >= y {
            writeln!(stdout, "1").unwrap();
        } else if y == 0 {
            writeln!(stdout, "1").unwrap();
        } else {
            writeln!(stdout, "2").unwrap();
        }
    }

    print!("{stdout}");
}
