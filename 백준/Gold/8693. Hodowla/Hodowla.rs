use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut nums: Vec<Vec<i32>> = (0..n)
        .map(|_| (0..n).map(|_| next().parse::<i32>().unwrap()).collect())
        .collect();

    let mut pre = vec![vec![0; n + 1]; n + 1];

    let m: usize = next().parse().unwrap();
    for _ in 0..m {
        let (y1, x1, y2, x2): (usize, usize, usize, usize) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );

        pre[x1 - 1][y1 - 1] += 1;
        pre[x2][y2] += 1;
        pre[x1 - 1][y2] -= 1;
        pre[x2][y1 - 1] -= 1;
    }

    // println!("{:?}", pre);
    for i in 0..=n {
        for j in 0..=n {
            if i + j == 0 {
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

    let mut res = String::new();

    for i in 0..n {
        for j in 0..n {
            write!(res, "{} ", (nums[i][j] + pre[i][j]) % 2).unwrap();
        }
        writeln!(res, "").unwrap();
    }

    print!("{res}");
}
