use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(n, nums));
}

fn solve(n: usize, nums: Vec<u32>) -> i8 {
    let mut winner = BinaryHeap::with_capacity(n);
    let mut loser = BinaryHeap::with_capacity(n);
    let mut tot = 0;
    for i in 0..n {
        tot += nums[i];
        if nums[i] > 0 {
            winner.push(nums[i]);
        }
        if nums[i] < n as u32 - 1 {
            loser.push((n as u32 - 1) - nums[i]);
        }
    }

    if tot != ((n - 1) * n / 2) as u32 {
        return -1;
    }

    while let Some(cur) = winner.pop() {
        if loser.len() < cur as usize {
            return -1;
        }

        let mut tmp = BinaryHeap::with_capacity(cur as usize);

        for _ in 0..cur {
            let nxt = loser.pop().unwrap();
            // i j 같으면 어카지
            if nxt > 1 {
                tmp.push(nxt - 1);
            }
        }
        loser.append(&mut tmp);
    }

    1
}
