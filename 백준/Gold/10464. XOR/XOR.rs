use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn xor_upto(k: u64) -> u64 {
    if k % 4 == 0 {
        return k;
    }
    if k % 4 == 1 {
        return 1;
    }
    if k % 4 == 2 {
        return k + 1;
    }
    0
}

fn range_xor(s: u64, f: u64) -> u64 {
    xor_upto(f) ^ xor_upto(s - 1)
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let t: usize = next().parse().unwrap();
    let mut stdout = String::with_capacity(t);

    for _ in 0..t {
        let s: u64 = next().parse().unwrap();
        let f: u64 = next().parse().unwrap();

        writeln!(stdout, "{}", range_xor(s, f)).unwrap();
    }

    print!("{stdout}")
}
