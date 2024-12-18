use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();

    let nums: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut l = 0;
    let mut cur = 0;
    let mut res = 0;

    for r in 0..n {
        cur += nums[r];

        while cur > k {
            cur -= nums[l];
            l += 1;
        }
        res = res.max(cur);
    }

    print!("{res}");
}
