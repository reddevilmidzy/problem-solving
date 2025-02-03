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

fn solve(n: usize, m: usize, nums: Vec<i32>) -> i32 {
    let mut pre = vec![0; n + 1];

    for i in 1..=n {
        pre[i] = pre[i - 1] + nums[i - 1];
    }

    let mut satisfied = vec![-1_000_000; n];

    for i in 1..n {
        let val = if i + 1 >= m {
            pre[i + 1] - pre[i + 1 - m]
        } else {
            -1_000_000
        };

        satisfied[i] = val.max(satisfied[i - 1] + nums[i]);
    }

    let mut res = 0;
    for i in 0..n {
        res = res.max(satisfied[i]);
    }
    res
}

#[test]
fn tmp() {
    assert_eq!(5, solve(8, 4, vec![-1, -1, 1, 1, 1, 1, -1, 2]));
    assert_eq!(1, solve(5, 5, vec![-1, -1, 1, 1, 1]));
    assert_eq!(1, solve(6, 4, vec![-8, -1, -3, 6, -1, -9]));
    assert_eq!(5, solve(7, 1, vec![-1, 1, 1, 1, 1, 1, -1]));
}
