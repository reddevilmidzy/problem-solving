use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn solve(n: i32) -> String {
    let mut res = String::new();

    for cnt in 0..n / 2 {
        let mut cur = cnt;
        let mut ans = String::new();

        for i in 1..n {
            write!(ans, "{} ", cur + 1).unwrap();
            if i % 2 != 0 {
                cur += i;
            } else {
                cur += n - 1;
                cur -= i;
            }
            cur %= n - 1;
        }

        writeln!(res, "{ans}{n}").unwrap();
    }

    res
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: i32 = next().parse().unwrap();

    print!("{}", solve(n));
}
