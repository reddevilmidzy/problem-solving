use std::collections::HashSet;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let n: usize = input.next().unwrap().unwrap().parse().unwrap();
    let nums: Vec<i32> = input.next().unwrap().unwrap().split_whitespace().map(|s| s.parse().unwrap()).collect();
    let m: usize = input.next().unwrap().unwrap().parse().unwrap();
    let choo: Vec<i32> = input.next().unwrap().unwrap().split_whitespace().map(|s| s.parse().unwrap()).collect();

    let mut can: HashSet<i32> = HashSet::new();
    can.insert(nums[0]);

    for i in 1..n {
        let mut tmp: HashSet<i32> = HashSet::new();
        tmp.insert(nums[i]);
        for &target in &can {
            tmp.insert((nums[i] - target).abs());
            tmp.insert(nums[i] + target);
        }
        can.extend(tmp);
    }

    for &c in &choo {
        if can.contains(&c) {
            print!("Y ");
        } else {
            print!("N ");
        }
    }
}
