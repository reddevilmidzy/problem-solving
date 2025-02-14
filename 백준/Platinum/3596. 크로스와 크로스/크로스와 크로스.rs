use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn mex(arr: Vec<u32>) -> u32 {
    for i in 0..arr.len() {
        if arr[i] != i as u32 {
            return i as u32;
        }
    }

    arr.len() as u32
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();

    print!("{}", solve(n))
}

fn solve(n: usize) -> u8 {
    let mut grundy = vec![0; n + 1];
    grundy[1] = 1;
    grundy[2] = 1;
    grundy[3] = 1;

    for i in 4..=n {
        let mut tmp = HashSet::new();

        for j in 0..i - 2 {
            let left_idx = if j <= 2 { 0 } else { j - 2 };
            let right_idx = i - (j + 3);
            let left = grundy[left_idx];
            let right = grundy[right_idx];
            // println!("i = {i}, left = {}, right = {}", j , i - j - 1);
            tmp.insert(left ^ right);
        }
        let mut tmp: Vec<u32> = tmp.into_iter().collect();
        tmp.sort();
        grundy[i] = mex(tmp);
    }

    if grundy[n] != 0 {
        return 1;
    }
    2
}

#[test]
fn tmp() {
    println!("{}", solve(10));
}
