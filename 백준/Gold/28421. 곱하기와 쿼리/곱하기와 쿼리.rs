use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let first_line = input.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();
    let _n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = 10_000;
    let q: usize = iter.next().unwrap().parse().unwrap();

    let mut nums: Vec<usize> = input.next().unwrap().unwrap().split_whitespace().map(|s| s.parse().unwrap()).collect();

    let mut cnt: Vec<i32> = vec![0; m + 1];

    for num in &nums {
        cnt[*num] += 1;
    }

    let mut res = String::new();

    for _ in 0..q {
        let line = input.next().unwrap().unwrap();
        let mut iter = line.split_whitespace();
        let u: usize = iter.next().unwrap().parse().unwrap();
        let v: usize = iter.next().unwrap().parse().unwrap();

        if u == 1 {
            let mut find = false;
            for i in 1..=m {
                if (v % i) == 0 && cnt[i] > 0 {
                    let j = v / i;
                    if j > m {
                        continue;
                    }
                    if i != j && cnt[j] > 0 {
                        res.push('1');
                        find = true;
                        break;
                    } else if i == j && cnt[j] > 1 {
                        res.push('1');
                        find = true;
                        break;
                    }
                }
            }
            if v == 0 && cnt[0] > 1 {
                res.push('1');
            } else if !find {
                res.push('0');
            }
            res.push('\n');
        } else if u == 2 {
            if nums[v - 1] != 0 {
                cnt[nums[v - 1]] -= 1;
            }
            nums[v - 1] = 0;
            cnt[0] += 1;
        }
    }

    print!("{res}");
}
