use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(n, nums));
}

fn solve(n: usize, mut nums: Vec<u32>) -> u32 {
    let mut res = 0;

    for i in 0..n - 2 {
        if nums[i + 1] > nums[i + 2] {
            let val = nums[i].min(nums[i + 1] - nums[i + 2]);
            res += val * 5;
            nums[i] -= val;
            nums[i + 1] -= val;
        }

        let val = nums[i].min(nums[i + 1]).min(nums[i + 2]);
        res += val * 7;
        nums[i] -= val;
        nums[i + 1] -= val;
        nums[i + 2] -= val;
    }

    for i in 0..n - 1 {
        let val = nums[i].min(nums[i + 1]);
        res += val * 5;
        nums[i] -= val;
        nums[i + 1] -= val;
    }

    for i in 0..n {
        res += nums[i] * 3;
    }

    res
}

#[test]
fn tmp() {
    assert_eq!(solve(4, vec![1, 5, 3, 7]), 41);
    assert_eq!(solve(4, vec![7, 3, 5, 1]), 41);
    assert_eq!(solve(3, vec![1, 0, 1]), 6);
    assert_eq!(solve(5, vec![1, 1, 1, 0, 2]), 13);
    assert_eq!(solve(4, vec![1, 2, 1, 1]), 12);
    assert_eq!(solve(4, vec![2, 4, 2, 2]), 24);
    assert_eq!(solve(4, vec![1, 4, 3, 3]), 26);
    assert_eq!(solve(4, vec![1, 3, 3, 1]), 19);
    assert_eq!(solve(4, vec![2, 5, 4, 2]), 31);
    assert_eq!(solve(7, vec![2, 3, 2, 3, 3, 2, 1]), 38);
    assert_eq!(solve(7, vec![1, 2, 3, 3, 2, 3, 2]), 38);
    assert_eq!(solve(4, vec![2, 3, 2, 1]), 19);
    assert_eq!(solve(3, vec![2, 1, 1]), 10);
    assert_eq!(solve(4, vec![2, 3, 2, 1]), 19);
    assert_eq!(solve(4, vec![1, 2, 3, 2]), 19);
    assert_eq!(solve(9, vec![4, 5, 4, 1, 2, 3, 5, 7, 9]), 97);
    assert_eq!(solve(9, vec![9, 7, 5, 3, 2, 1, 4, 5, 4]), 97);
    assert_eq!(solve(4, vec![1, 2, 3, 2]), 19);
    assert_eq!(solve(4, vec![2, 4, 5, 2]), 31);
    assert_eq!(solve(4, vec![3, 3, 4, 1]), 26);
}
