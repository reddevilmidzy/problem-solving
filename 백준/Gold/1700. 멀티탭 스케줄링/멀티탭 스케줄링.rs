use std::collections::{BinaryHeap, VecDeque};
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();
    let nums: Vec<usize> = (0..k).map(|_| next().parse().unwrap()).collect();

    print!("{}", solve(n, k, nums));
}

fn solve(n: usize, k: usize, nums: Vec<usize>) -> i32 {
    let mut res = 0;
    let mut idx = vec![VecDeque::new(); k + 1];
    let mut used = vec![false; k + 1];

    for i in 0..k {
        idx[nums[i]].push_back(i);
    }

    let mut hq = BinaryHeap::with_capacity(n);
    let mut cnt = 0;

    for i in 0..k {
        idx[nums[i]].pop_front();
        let val = *idx[nums[i]].front().unwrap_or(&k);
        if cnt >= n && !used[nums[i]] {
            res += 1;

            loop {
                let (_p_idx, p_val) = hq.pop().unwrap();
                if used[p_val] {
                    used[p_val] = false;
                    cnt -= 1;
                    break;
                }
            }
        }
        hq.push((val, nums[i]));
        if !used[nums[i]] {
            cnt += 1;
        }
        used[nums[i]] = true;
    }

    res
}
