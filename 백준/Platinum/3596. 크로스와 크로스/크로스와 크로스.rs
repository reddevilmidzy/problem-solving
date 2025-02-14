use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn mex(arr: Vec<u8>) -> u8 {
    for i in 0..arr.len() {
        if arr[i] != i as u8 {
            return i as u8;
        }
    }

    arr.len() as u8
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();

    print!("{}", solve(n))
}

fn solve(n: usize) -> u8 {
    let mut grundy = vec![0u8; n + 1];
    grundy[1] = 1;
    grundy[2] = 1;
    grundy[3] = 1;

    for i in 4..=n {
        let mut tmp = HashSet::new();

        for j in 0..(i + 5) / 2 - 2 {
            let left_idx = if j <= 2 { 0 } else { j - 2 };
            let right_idx = i - (j + 3);
            let left = grundy[left_idx];
            let right = grundy[right_idx];
            tmp.insert(left ^ right);
        }
        let mut tmp: Vec<u8> = tmp.into_iter().collect();
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
