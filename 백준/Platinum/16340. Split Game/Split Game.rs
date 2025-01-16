use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn mex(mut arr: Vec<u32>) -> u32 {
    arr.sort();

    for i in 0..arr.len() {
        if arr[i] != i as u32 {
            return i as u32;
        }
    }
    arr.len() as u32
}

fn sprague_grundy() -> Vec<u32> {
    let m: usize = 2000;
    let mut grundy = vec![0u32; m + 1];
    grundy[2] = 1;

    for i in 3..=m {
        let mut tmp = HashSet::new();
        for j in 1..i {
            tmp.insert(grundy[if (i / j) % 2 == 1 { j } else { 0 }] ^ grundy[i % j]);
        }

        let tmp: Vec<u32> = tmp.into_iter().collect();
        grundy[i] = mex(tmp);
    }

    grundy
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();
    let nums: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();

    let grundy = sprague_grundy();

    let mut res: u32 = 0;
    for num in nums {
        res ^= grundy[num];
    }

    if res != 0 {
        print!("First");
    } else {
        print!("Second");
    }
}
