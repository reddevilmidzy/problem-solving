use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut stdout = String::new();

    let t: usize = next().parse().unwrap();
    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
        writeln!(stdout, "{}", solve(nums)).unwrap();
    }
    print!("{}", stdout);
}

fn solve(nums: Vec<u32>) -> String {
    let mut res = 0u32;
    let mut flag = false;
    for num in nums {
        flag |= num != 1;
        res ^= num;
    }

    if (res == 0) ^ flag {
        return "John".to_string();
    }
    "Brother".to_string()
}

#[test]
fn tmp() {
    let john = "John".to_string();
    let bro = "Brother".to_string();
    assert_eq!(john, solve(vec![3, 5, 1]));
    assert_eq!(bro, solve(vec![1]));
    assert_eq!(bro, solve(vec![5, 4, 1])); // 0
    assert_eq!(john, solve(vec![1, 1])); // 0
    assert_eq!(bro, solve(vec![2, 2])); // 0
    assert_eq!(bro, solve(vec![9, 8, 9, 8, 9, 9])); // 0
    assert_eq!(bro, solve(vec![1])); // 1
    assert_eq!(john, solve(vec![2])); // 2
    assert_eq!(john, solve(vec![1, 2])); // 3
    assert_eq!(john, solve(vec![1, 2, 3, 4])); // 4
}
