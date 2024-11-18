use std::io::{self, BufRead};

fn cal_dist(st: &Vec<i32>, ed: &Vec<i32>) -> i32 {
    (st[0] - ed[0]).abs() + (st[1] - ed[1]).abs()
}

fn find(y: usize, x: usize, n: usize, m: usize, dp: &mut Vec<Vec<i32>>, nums: &Vec<Vec<i32>>) -> i32 {
    if y == m || x == m {
        return 0;
    }

    if dp[y][x] != -1 {
        return dp[y][x];
    }

    let nxt = y.max(x) + 1;

    let y_dist = if y == 0 { cal_dist(&vec![1, 1], &nums[nxt]) } else { cal_dist(&nums[y], &nums[nxt]) };
    let x_dist = if x == 0 { cal_dist(&vec![n as i32, n as i32], &nums[nxt]) } else { cal_dist(&nums[x], &nums[nxt]) };

    dp[y][x] = (find(nxt, x, n, m, dp, &nums) + y_dist).min(find(y, nxt, n, m, dp, &nums) + x_dist);
    dp[y][x]
}


fn trace(y: usize, x: usize, n: usize, m: usize, dp: Vec<Vec<i32>>, nums: Vec<Vec<i32>>) {
    if y == m || x == m {
        return;
    }
    let nxt: usize = x.max(y) + 1;

    let y_dist = if y == 0 { cal_dist(&vec![1, 1], &nums[nxt]) } else { cal_dist(&nums[y], &nums[nxt]) };
    let x_dist = if x == 0 { cal_dist(&vec![n as i32, n as i32], &nums[nxt]) } else { cal_dist(&nums[x], &nums[nxt]) };

    if dp[nxt][x] + y_dist > dp[y][nxt] + x_dist {
        println!("{}", 2);
        trace(y, nxt, n, m, dp, nums);
    } else {
        println!("{}", 1);
        trace(nxt, x, n, m, dp, nums);
    }
    return;
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();
    let n: usize = input.next().unwrap().unwrap().parse().unwrap();
    let m: usize = input.next().unwrap().unwrap().parse().unwrap();

    let mut dp = vec![vec![-1; m + 1]; m + 1];

    let mut nums = vec![vec![-1; 2]; m + 1];

    for i in 1..=m {
        let line = input.next().unwrap().unwrap();
        let event: Vec<i32> = line.split_whitespace().map(|s| s.parse().unwrap()).collect();
        nums[i] = event;
    }
    let res = find(0, 0, n, m, &mut dp, &nums);

    // println!("{:?}", dp);
    println!("{res}");
    trace(0, 0, n, m, dp, nums);
}
