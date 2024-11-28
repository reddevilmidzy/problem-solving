use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: i64 = next().parse().unwrap();
    let mut nums: Vec<i64> = (0..n).map(|_| next().parse().unwrap()).collect();

    // pre[i]까지 최소거리로 오는데 얻는 점수
    let mut pre: Vec<i64> = vec![0; n];
    let mut suf: Vec<i64> = vec![0; n];
    let mut res: Vec<i64> = vec![0; n];

    res[0] = nums[0] * k;
    for i in 1..n.min(k as usize) {
        pre[i] = pre[i - 1] + nums[i - 1];
        res[i] = pre[i] + (nums[i] * (k - i as i64));
    }

    nums.reverse();
    res[0] = res[0].max(nums[0] * k);

    for i in 1..n.min(k as usize) {
        suf[i] = suf[i - 1] + nums[i - 1];
        res[i] = res[i].max(suf[i] + (nums[i] * (k - i as i64)));
    }

    let ans = res.iter().max().unwrap();
    print!("{ans}");
}
