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

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();

    let mut grundy = vec![0u32; n + 1];
    grundy[0] = 0;
    grundy[1] = 0;
    grundy[2] = 1;

    for i in 3..=n {
        let mut nums: HashSet<u32> = HashSet::new();
        for j in 0..i - 1 {
            nums.insert(grundy[j] ^ grundy[i - 2 - j]);
        }

        let nums: Vec<u32> = nums.into_iter().collect();
        grundy[i] = mex(nums);
    }

    if grundy[n] != 0 {
        print!("1");
    } else {
        print!("2");
    }
}
