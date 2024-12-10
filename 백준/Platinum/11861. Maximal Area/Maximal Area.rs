use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();

    let nums: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut r_stk: Vec<usize> = Vec::new();
    let mut l_stk: Vec<usize> = Vec::new();

    let mut r_idx: Vec<i32> = vec![n as i32; n];
    let mut l_idx: Vec<i32> = vec![-1; n];

    for i in 0..n {
        while !r_stk.is_empty() && nums[*r_stk.last().unwrap()] > nums[i] {
            r_idx[r_stk.pop().unwrap()] = i as i32;
        }
        r_stk.push(i);

        while !l_stk.is_empty() && nums[*l_stk.last().unwrap()] > nums[n - i - 1] {
            l_idx[l_stk.pop().unwrap()] = (n - i - 1) as i32;
        }
        l_stk.push(n - i - 1);
    }

    let mut res = 0;

    for i in 0..n {
        res = res.max((r_idx[i] as i64 - l_idx[i] as i64 - 1) * nums[i] as i64);
    }
    print!("{res}")
}
