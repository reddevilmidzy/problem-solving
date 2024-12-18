use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};
use std::ops::Add;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut hq = BinaryHeap::with_capacity(4);

    for num in nums {
        if hq.len() < 4 {
            hq.push(num);
        } else if hq.peek().unwrap() > &num {
            hq.pop();
            hq.push(num);
        }
    }

    let mut tmp = Vec::with_capacity(6);
    let hq = Vec::from(hq);
    for i in 0..hq.len() {
        for j in i + 1..hq.len() {
            tmp.push(hq[i].to_string().add(&*hq[j].to_string()).parse::<i32>().unwrap());
            tmp.push(hq[j].to_string().add(&*hq[i].to_string()).parse::<i32>().unwrap());
        }
    }

    tmp.sort();
    print!("{}", tmp[2]);
}
