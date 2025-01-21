use std::collections::HashSet;
use std::io::{read_to_string, stdin};

// 1 0 2 1 3 2 4 3
// i i-1 형태

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
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(n, nums));
}

fn solve(_n: usize, nums: Vec<u32>) -> String {
    let mut res =0 ;

    for num in nums {
        res ^= find_grundy(num);
    }
    if res != 0 {
        "koosaga".to_string()
    } else {
        "cubelover".to_string()
    }
}

fn find_grundy(num: u32) -> u32 {
    if num % 2 != 0 {
        return (num + 1) / 2;
    }
    (num - 1) / 2
}

fn get_grundy() -> Vec<u32> {
    let n = 40;
    let mut grundy = vec![0; n + 1];
    grundy[1] = 1;
    grundy[3] = 2;

    for i in 4..=n {
        let mut nums: HashSet<u32> = HashSet::new();
        for j in 1..=(i-1)/2 {
            nums.insert(grundy[i - j * 2]);
        }
        if i % 2 != 0 {
            nums.insert(grundy[0]);
        }
        let nums: Vec<u32> = nums.into_iter().collect();
        grundy[i] = mex(nums);
    }

    grundy
}

#[test]
fn tmp() {
    let koo = "koosaga".to_string();
    let cub = "cubelover".to_string();
    assert_eq!(koo, solve(1, vec![1]));
    assert_eq!(cub, solve(2, vec![1, 1]));
    assert_eq!(koo, solve(2, vec![1,2 ]));
    assert_eq!(koo, solve(4, vec![1,2,3,4]));
    assert_eq!(cub, solve(6, vec![9,8,9,8,9,9]));
}
