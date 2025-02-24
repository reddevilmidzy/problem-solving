use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let _n: u32 = next().parse().unwrap();
    let s = &next()[1..];
    print!("{}", solve(s));
}

fn solve(binary_n: &str) -> u64 {
    let mut ans = 0;
    let mut flag = false;
    for ch in binary_n.chars().rev() {
        if ch == '1' && !flag {
            ans += 1;
            flag = true;
        }
        if ch == '0' && flag {
            ans += 1;
        }
    }

    ans
}
