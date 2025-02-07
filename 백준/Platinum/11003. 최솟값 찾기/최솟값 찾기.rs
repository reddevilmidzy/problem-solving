use std::collections::VecDeque;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();

    print!("{}", solve(n, m, nums));
}

fn solve(n: usize, m: usize, nums: Vec<i32>) -> String {
    let mut res = String::new();

    let mut deque: VecDeque<(i32, usize)> = VecDeque::new();

    for i in 0..n {
        while !deque.is_empty() && deque.back().unwrap().0 >= nums[i] {
            deque.pop_back();
        }
        deque.push_back((nums[i], i));
        while i >= m && deque.front().unwrap().1 <= i - m {
            deque.pop_front();
        }

        write!(res, "{} ", deque.front().unwrap().0).unwrap();
    }

    res
}

#[test]
fn tmp() {
    print!("{}", solve(12, 3, vec![1, 5, 2, 3, 6, 2, 3, 7, 3, 5, 2, 6]))
}
