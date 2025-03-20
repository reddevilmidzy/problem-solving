use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn generate(n: usize, pre: &mut Vec<Vec<i64>>) {
    for i in 0..=n {
        for j in 0..=n {
            if i == 0 && j == 0 {
                continue;
            } else if i == 0 {
                pre[i][j] += pre[i][j - 1];
            } else if j == 0 {
                pre[i][j] += pre[i - 1][j];
            } else {
                pre[i][j] += pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1];
            }
        }
    }

    for i in 0..=n {
        for j in 0..=n {
            if i == 0 && j == 0 {
                continue;
            } else if i == 0 {
                pre[i][j] += pre[i][j - 1];
            } else if j == 0 {
                pre[i][j] += pre[i - 1][j];
            } else {
                pre[i][j] += pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1];
            }
        }
    }
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut stdout = String::new();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut nums = vec![vec![0; n + 1]; n + 1];

    for i in 1..=n {
        for j in 1..=n {
            nums[i][j] = next().parse().unwrap();
            nums[i][j] += nums[i - 1][j] + nums[i][j - 1] - nums[i - 1][j - 1];
        }
    }

    let mut pre = vec![vec![0i64; n + 2]; n + 2];

    let mut first = true;
    for _ in 0..m {
        let cmd = next();
        if cmd == "1" {
            let (y1, x1): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
            let (y2, x2): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());

            let k: i64 = next().parse().unwrap();
            pre[y1 + 1][x1 + 1] += k;
            pre[y2 + 2][x2 + 2] += k;

            pre[y1 + 1][x2 + 2] -= k;
            pre[y2 + 2][x1 + 1] -= k;
            continue;
        }
        if first {
            generate(n, &mut pre);
            first = false;
        }
        let (y1, x1): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        let (y2, x2): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        let t1 = pre[y2 + 1][x2 + 1] - pre[y2 + 1][x1] - pre[y1][x2 + 1] + pre[y1][x1];
        let t2 = nums[y2 + 1][x2 + 1] - nums[y2 + 1][x1] - nums[y1][x2 + 1] + nums[y1][x1];
        writeln!(stdout, "{}", t1 + t2).unwrap();
    }

    print!("{stdout}");
}
