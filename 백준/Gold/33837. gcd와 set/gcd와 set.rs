use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn gcd(a: u32, b: u32) -> u32 {
    if b == 0 {
        return a;
    }
    gcd(b, a % b)
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut val = 0;
    for i in 0..n {
        val = gcd(val, nums[i]);
    }

    if n == 1 {
        print!("{}", nums[0]);
        return;
    }
    let nums: HashSet<u32> = nums.into_iter().collect();

    let mut nums = nums.into_iter().collect::<Vec<_>>();
    nums.sort_unstable();
    for i in 0..nums.len() {
        nums[i] /= val;
    }
    if nums[0] == *nums.last().unwrap() {
        print!("{}", nums[0] * 2 * val);
        return;
    }
    let mut res = *nums.last().unwrap() + 1;
    for i in 2..=*nums.last().unwrap() {
        if *nums.last().unwrap() % i == 0 {
            let mut a = 0;
            let mut b = 0;

            for j in 0..nums.len() {
                if nums[j] % i == 0 {
                    a = gcd(a, nums[j]);
                } else {
                    b = gcd(b, nums[j]);
                }
            }
            res = res.max(a + b);
            if b == 0 {
                res = res.max(a + *nums.last().unwrap());
            }
        }
    }
    print!("{}", res * val);
}
