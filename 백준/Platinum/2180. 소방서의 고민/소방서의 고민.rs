use std::io::{read_to_string, stdin};

const MODU: u32 = 40_000;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();

    let mut nums: Vec<(u32, u32)> = (0..n)
        .map(|_| (next().parse().unwrap(), next().parse().unwrap()))
        .collect();

    nums.sort_by_key(|&(a, b)| ((b as f64 / a as f64) * 100.0) as u32);
    let mut res = 0;

    for (a, b) in nums {
        res += (res * a) + b;
        res %= MODU;
    }

    print!("{res}");
}
