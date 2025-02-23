use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<(i32, i32)> = (0..n)
        .map(|_| (next().parse().unwrap(), next().parse().unwrap()))
        .collect();

    let mut ans = Vec::new();
    for i in 0..n {
        let std = nums[i].0;
        let mut tot = 0;

        for j in 0..n {
            if nums[j].0 < std {
                continue;
            } else {
                tot += 0.max(std - nums[j].1);
            }
        }
        if tot != 0 {
            ans.push((-tot, nums[i].0))
        }
    }

    ans.sort();
    if !ans.is_empty() {
        print!("{}", ans[0].1);
    } else {
        print!("0");
    }
}
