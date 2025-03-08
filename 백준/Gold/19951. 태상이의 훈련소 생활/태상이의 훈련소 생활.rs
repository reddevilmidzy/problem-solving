use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();
    let mut pre: Vec<i32> = vec![0; n + 1];
    for _ in 0..m {
        let (u,v,w): (usize, usize, i32) = (next().parse().unwrap(), next().parse().unwrap(), next().parse().unwrap());

        pre[u-1] += w;
        pre[v] -= w;
    }

    for i in 1..n {
        pre[i] += pre[i-1]
    }

    let mut res = String::new();
    for i in 0..n {
        write!(res, "{} ", nums[i] + pre[i]).unwrap();
    }

    print!("{res}");
}
