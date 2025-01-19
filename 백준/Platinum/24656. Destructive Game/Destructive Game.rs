use std::io::{read_to_string, stdin};

fn find_grundy(a: u32, b: u32) -> u32 {
    if b % 2 != 0 {
        return a % 2;
    }
    let a = a % (b + 1);
    if a == b {
        return 2;
    }
    a % 2
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();
    let mut res: u32 = 0;

    for _ in 0..n {
        let a: u32 = next().parse().unwrap();
        let b: u32 = next().parse().unwrap();

        res ^= find_grundy(a, b);
    }

    if res != 0 {
        print!("Alice");
    } else {
        print!("Bob");
    }
}
