use std::io::{read_to_string, stdin};
use std::ops::Add;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    print!("{}", solve(n));
}

fn solve(n: usize) -> String {
    let mut res = vec![0; n];
    res[0] = 3;
    for i in 1..n {
        res[i] = i * 2;
    }
    if n % 3 == 2 {
        res[n - 1] += 4;
    }

    res.iter().map(|x| x.to_string().add(" ")).collect()
}
