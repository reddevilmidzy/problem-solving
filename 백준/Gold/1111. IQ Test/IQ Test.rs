use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(n, nums));
}

fn solve(n: usize, nums: Vec<i32>) -> String {
    if n == 1 {
        return "A".to_string();
    }
    if n == 2 {
        if nums[0] == nums[1] {
            return nums[0].to_string();
        }
        return "A".to_string();
    }

    let mut diff = Vec::new();
    for i in 0..n - 1 {
        diff.push(nums[i + 1] - nums[i]);
    }

    // println!("nums = {:?}", nums);
    // println!("diff = {:?}", diff);
    if diff[0] == 0 {
        for i in 1..diff.len() {
            if diff[i] != 0 {
                return "B".to_string();
            }
        }
        return nums[0].to_string();
    }
    let a = diff[1] / diff[0];
    let b = nums[1] - nums[0] * a;

    for i in 0..n - 1 {
        if nums[i + 1] != nums[i] * a + b {
            return "B".to_string();
        }
    }

    (nums[n - 1] * a + b).to_string()
}

#[test]
fn tmp() {
    assert_eq!("121".to_string(), solve(4, vec![1, 4, 13, 40]));
    assert_eq!("6".to_string(), solve(5, vec![1, 2, 3, 4, 5]));
    assert_eq!("96".to_string(), solve(5, vec![3, 6, 12, 24, 48]));
    assert_eq!("A".to_string(), solve(1, vec![0]));
    assert_eq!("A".to_string(), solve(2, vec![-1, 2]));
}
