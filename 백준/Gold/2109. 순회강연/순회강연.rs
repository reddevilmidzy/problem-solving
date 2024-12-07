use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();

    let mut nums: Vec<[i32; 2]> = (0..n)
        .map(|_| [next().parse().unwrap(), next().parse().unwrap()])
        .collect();

    nums.sort_unstable_by_key(|x| x[1]);

    let mut hq: BinaryHeap<i32> = BinaryHeap::new();

    for num in nums {
        if hq.len() < num[1] as usize {
            hq.push(-num[0]);
        } else {
            if !hq.is_empty() && -hq.peek().unwrap() <= num[0] && hq.len() >= num[1] as usize {
                hq.pop();
            }
            if hq.len() < num[1] as usize {
                hq.push(-num[0]);
            }
        }
    }
    let mut res = 0;
    while !hq.is_empty() {
        res -= hq.pop().unwrap();
    }

    print!("{res}");
}
