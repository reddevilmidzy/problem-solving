use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: i32 = next().parse().unwrap();

    let mut nums = Vec::new();

    for _ in 0..n {
        let (u, v): (i32, i32) = (next().parse().unwrap(), next().parse().unwrap());
        nums.push((u, v));
    }
    nums.sort_unstable();

    let mut pre = -1;
    let mut res = 0;

    for (st, ed) in nums {
        if ed <= pre {
            continue;
        } else if pre < st {
            let tmp = (ed - st  + (m - 1)) / m;
            res += tmp;
            pre = st + (m * tmp) - 1;
        } else if st <= pre {
            let tmp = (ed - pre - 1 + (m - 1)) / m;
            res += tmp;
            pre = pre + (m * tmp);
        }
    }
    print!("{res}");
}
