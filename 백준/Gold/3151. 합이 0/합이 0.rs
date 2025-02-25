use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(nums));
}

fn solve(nums: Vec<i32>) -> u64 {
    let mut res = 0;
    let mut zero = 0;
    let mut neg = Vec::new();
    let mut pos = Vec::new();

    for num in nums {
        if num < 0 {
            neg.push(num);
        } else if num > 0 {
            pos.push(num);
        } else {
            zero += 1;
        }
    }

    // nC3
    if zero >= 3 {
        res += (zero * (zero - 1) * (zero - 2)) / (6);
    }
    neg.sort();
    pos.sort();

    // -x +x + 0 조합
    // [-2,-2,0,0,2,2,2,2]

    for &num in &neg {
        let l = bisect_left(&pos, -num);
        let r = bisect_right(&pos, -num);
        res += zero * (r - l) as u64;
    }

    // -x-y+z 조합
    // -x+y+z 조합
    for i in 0..neg.len() {
        for j in i + 1..neg.len() {
            let num = neg[i] + neg[j];
            let l = bisect_left(&pos, -num);
            let r = bisect_right(&pos, -num);
            res += (r - l) as u64;
        }
    }

    for i in 0..pos.len() {
        for j in i + 1..pos.len() {
            let num = pos[i] + pos[j];
            let l = bisect_left(&neg, -num);
            let r = bisect_right(&neg, -num);
            res += (r - l) as u64;
        }
    }

    res
}

fn bisect_left(nums: &Vec<i32>, target: i32) -> usize {
    let mut low = 0;
    let mut high = nums.len();

    while low < high {
        let mid = (low + high) / 2;
        if nums[mid] < target {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    low
}

fn bisect_right(nums: &Vec<i32>, target: i32) -> usize {
    let mut low = 0;
    let mut high = nums.len();

    while low < high {
        let mid = (low + high) / 2;
        if nums[mid] <= target {
            low = mid + 1;
        } else {
            high = mid;
        }
    }

    low
}
