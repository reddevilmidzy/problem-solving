use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();
    let l: usize = next().parse().unwrap();

    let mut nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    let mut coke = vec![0; n + 1];
    for _ in 0..k {
        let idx: usize = next().parse().unwrap();
        coke[idx - 1] += 1;
        coke[(idx + l - 1).min(n)] -= 1;
    }
    for i in 1..n {
        coke[i] += coke[i - 1];
    }
    coke[n] = i32::MAX;
    nums.sort_unstable();
    coke.sort_unstable();

    let mut res = 0u64;
    for i in 0..n {
        res += nums[i] as u64 >> 32.min(coke[i] as u64);
    }

    print!("{res}");
}
