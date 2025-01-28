use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(nums));
}

fn solve(nums: Vec<u32>) -> String {
    let mut res = 0u32;
    let mut flag = false;
    for num in nums {
        flag |= num != 1;
        res ^= num;
    }

    if (res == 0) ^ flag {
        return "koosaga".to_string();
    }
    "cubelover".to_string()
}

#[test]
fn tmp() {
    let koo = "koosaga".to_string();
    let cub = "cubelover".to_string();
    assert_eq!(cub, solve(vec![5,4,1])); // 0
    assert_eq!(koo, solve(vec![1, 1])); // 0
    assert_eq!(cub, solve(vec![2, 2])); // 0
    assert_eq!(cub, solve(vec![9, 8, 9, 8, 9, 9])); // 0
    assert_eq!(cub, solve(vec![1])); // 1
    assert_eq!(koo, solve(vec![2])); // 2
    assert_eq!(koo, solve(vec![1, 2])); // 3
    assert_eq!(koo, solve(vec![1, 2, 3, 4])); // 4
}
