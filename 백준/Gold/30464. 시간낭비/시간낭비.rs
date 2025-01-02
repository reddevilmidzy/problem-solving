use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();
    // dp1[i] = 0에서 시작해서 i까지 가는데 걸리는 시간
    let mut dp1 = vec![-1_000_000; n];
    dp1[0] = 0;

    for i in 0..n {
        if i + nums[i] < n && dp1[i] != -1 && nums[i] != 0 {
            dp1[i + nums[i]] = dp1[i + nums[i]].max(dp1[i] + 1);
        }
    }

    // i에서 시작해서 n-1으로 가는데 걸리는 시간
    for i in (0..n - 1).rev() {
        if nums[i] <= i && nums[i] != 0 {
            dp1[i - nums[i]] = dp1[i - nums[i]].max(dp1[i] + 1);
        }
    }

    for i in 0..n {
        if i + nums[i] < n && nums[i] != 0 {
            dp1[i + nums[i]] = dp1[i + nums[i]].max(dp1[i] + 1);
        }
    }

    if dp1[n - 1] > 0 {
        print!("{}", dp1[n - 1]);
    } else {
        print!("-1");
    }
}
