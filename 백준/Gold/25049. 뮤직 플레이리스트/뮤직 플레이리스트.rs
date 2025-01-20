use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<i64> = (0..n).map(|_| next().parse().unwrap()).collect();
    print!("{}", solve(n, nums));
}

fn solve(n: usize, nums: Vec<i64>) -> i64 {

    let mut tot = nums[0];
    let mut go = vec![0i64; n];
    let mut back = vec![0i64; n];

    let mut go_pre = nums[0];
    go[0] = go_pre;
    let mut back_pre = nums[n - 1];
    back[n-1] = back_pre;

    for i in 1..n {
        tot += nums[i];

        go_pre = nums[i].max(nums[i] + go_pre);
        go[i] = go[i - 1].max(go_pre);

        back_pre = nums[n - i - 1].max(nums[n - i - 1] + back_pre);
        back[n - i - 1] = back[n - i].max(back_pre);
    }

    let mut tmp = 0.max(go[n-1]);
    for i in 0..n-1 {
        tmp = tmp.max(go[i] + back[i + 1]);
    }
    tot + tmp
}
