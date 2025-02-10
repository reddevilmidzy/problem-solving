use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut nums: Vec<(u32, u32)> = (0..n)
        .map(|_| (next().parse().unwrap(), next().parse().unwrap()))
        .collect();
    // 정렬...?

    nums.sort();
    let (l, p): (u32, u32) = (next().parse().unwrap(), next().parse().unwrap());
    nums.push((l, 0));
    print!("{}", solve(l, p, nums));
}

fn solve(l: u32, p: u32, nums: Vec<(u32, u32)>) -> i32 {
    let mut hq: BinaryHeap<u32> = BinaryHeap::new();
    let mut cnt = 0;
    let mut cur_dist = p;

    for (dist, fuel) in nums {
        if cur_dist >= l {
            break;
        }
        while cur_dist < dist && !hq.is_empty() {
            cnt += 1;
            cur_dist += hq.pop().unwrap();
        }
        if cur_dist < dist {
            break;
        }
        hq.push(fuel);
    }

    if cur_dist >= l {
        cnt
    } else {
        -1
    }
}
