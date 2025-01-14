use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();
    let k: u64 = next().parse().unwrap();

    let a: Vec<u64> = (0..n).map(|_| next().parse().unwrap()).collect();
    let b: Vec<u64> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut pre_a = a[0];
    let mut pre_b = b[0];

    for i in 1..n {
        (pre_a, pre_b) = (pre_a.min(pre_b + k) + a[i], pre_b.min(pre_a + k) + b[i]);
    }

    print!("{}", pre_a.min(pre_b));
}
