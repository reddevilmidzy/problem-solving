use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn lower_bound(nums: &Vec<usize>, target: usize) -> usize {
    let mut low: i32 = 0;
    let mut high: i32 = nums.len() as i32 - 1;

    while low <= high {
        let mid = (low + high) / 2;
        if nums[mid as usize] < target {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    low as usize
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut nums: Vec<(usize, usize)> = (0..n).map(|_| (next().parse().unwrap(), next().parse().unwrap())).collect();

    nums.sort();

    let mut dp = Vec::new();
    let mut trace = Vec::new();

    for (_u, v) in &nums {
        let k = lower_bound(&dp, *v);
        if dp.len() <= k {
            dp.push(*v);
            trace.push((dp.len() - 1, *v));
        } else {
            dp[k] = *v;
            trace.push((k, *v));
        }
    }

    let mut idx = dp.len() - 1;
    let mut tmp = Vec::with_capacity(idx + 1);

    for i in (0..n).rev() {
        if trace[i].0 == idx {
            tmp.push(trace[i].1);
            if idx == 0 {
                break;
            }
            idx -= 1;
        }
    }

    let s: HashSet<usize> = tmp.into_iter().collect();

    let mut res = String::new();
    for (u, v) in &nums {
        if !s.contains(v) {
            res.push_str(u.to_string().as_str());
            res.push('\n');
        }
    }

    println!("{}", n - dp.len());
    print!("{res}");
}
