use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let nums: Vec<Vec<u64>> = (0..n)
        .map(|_| (0..m).map(|_| next().parse::<u64>().unwrap()).collect())
        .collect();

    let mut res = 0;

    for i in 0..n {
        let mut tmp = 0;
        for j in 0..m {
            tmp += nums[i][j];
        }
        res ^= tmp;
    }

    if res != 0 {
        print!("august14");
    } else {
        print!("ainta");
    }
}
