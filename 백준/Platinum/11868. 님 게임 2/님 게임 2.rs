use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();

    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut res = 0;
    for num in nums {
        res ^= num;
    }
    if res == 0 {
        print!("cubelover");
    } else {
        print!("koosaga");
    }
}
