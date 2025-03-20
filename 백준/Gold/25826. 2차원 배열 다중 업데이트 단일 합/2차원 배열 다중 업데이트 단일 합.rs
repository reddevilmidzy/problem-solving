use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let nums: Vec<Vec<i32>> = (0..n)
        .map(|_| (0..n).map(|_| next().parse::<i32>().unwrap()).collect())
        .collect();

    let mut pre = vec![vec![0i64; n + 1]; n + 1];

    for _ in 0..m - 1 {
        next();
        let (y1, x1): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        let (y2, x2): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());

        let k: i64 = next().parse().unwrap();
        pre[y1][x1] += k;
        pre[y2 + 1][x2 + 1] += k;

        pre[y1][x2 + 1] -= k;
        pre[y2 + 1][x1] -= k;
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

    next();

    let (y1, x1): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
    let (y2, x2): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());

    let mut res = 0;

    for i in y1..=y2 {
        for j in x1..=x2 {
            res += nums[i][j] as i64 + pre[i][j];
        }
    }

    print!("{res}");
}
