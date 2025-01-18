use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    let mut res = 0;

    for num in &nums {
        res ^= *num;
    }
    if res == 0 {
        print!("0");
        return;
    }
    let mut cnt = -1;
    while res > 0 {
        res /= 2;
        cnt += 1;
    }

    let mut ans = 0;
    for num in nums {
        if num & (1 << cnt) > 0 {
            ans += 1;
        }
    }

    print!("{ans}");
}
