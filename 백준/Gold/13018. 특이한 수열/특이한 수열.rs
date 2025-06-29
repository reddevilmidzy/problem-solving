use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: u32 = next().parse().unwrap();
    let k: u32 = next().parse().unwrap();
    let mut res = String::new();

    if n == k {
        print!("Impossible");
        return;
    }
    write!(&mut res, "{} ", n - k).unwrap();

    for i in 1..n - k {
        write!(&mut res, "{} ", i).unwrap();
    }
    for i in n - k + 1..=n {
        write!(&mut res, "{} ", i).unwrap();
    }
    print!("{}", res);
}
