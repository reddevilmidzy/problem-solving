use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let mut stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();

    let mut res = String::new();
    if n == 1 {
        writeln!(res, "1\n1 1").unwrap();
    } else {
        writeln!(res, "{}", n + (n - 2)).unwrap();
        for i in 1..=n {
            writeln!(res, "1 {i}").unwrap();
            if 1 < i && i < n {
                writeln!(res, "{n} {i}").unwrap();
            }
        }
    }

    print!("{res}");
}
