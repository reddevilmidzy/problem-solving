use std::collections::HashMap;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let t: i64 = next().parse().unwrap();
    let n: usize = next().parse().unwrap();
    let a: Vec<i64> = (0..n).map(|_| next().parse().unwrap()).collect();
    let m: usize = next().parse().unwrap();
    let b: Vec<i64> = (0..m).map(|_| next().parse().unwrap()).collect();

    let mut res: i64 = 0;
    let mut a_pre: Vec<i64> = vec![0; n + 1];

    for i in 1..=n {
        a_pre[i] = a_pre[i - 1] + a[i - 1];
    }

    let mut b_pre: Vec<i64> = vec![0; m + 1];
    for i in 1..=m {
        b_pre[i] = b_pre[i - 1] + b[i - 1];
    }

    let mut nums: HashMap<i64, i64> = HashMap::new();

    for i in 0..=n {
        for j in (i + 1)..=n {
            let val = a_pre[j] - a_pre[i];
            if !nums.contains_key(&val) {
                nums.insert(val, 1);
            } else {
                nums.insert(val, *nums.get(&val).unwrap() + 1);
            }
        }
    }

    for i in 0..=m {
        for j in (i + 1)..=m {
            let x = t - (b_pre[j] - b_pre[i]);
            if nums.contains_key(&x) {
                res += *nums.get(&x).unwrap();
            }
        }
    }

    print!("{res}")
}
