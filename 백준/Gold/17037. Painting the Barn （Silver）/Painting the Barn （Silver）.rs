use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let m = 1000;
    let n: usize = next().parse().unwrap();
    let k: i32 = next().parse().unwrap();

    let mut pre = vec![vec![0; m + 1]; m + 1];
    for _ in 0..n {
        let (x1, y1, x2, y2): (usize, usize, usize, usize) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );

        pre[y1][x1] += 1;
        pre[y2][x2] += 1;

        pre[y1][x2] -= 1;
        pre[y2][x1] -= 1;
    }

    for i in 0..=m {
        for j in 0..=m {
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

    let mut res = 0;
    for i in 0..=m {
        for j in 0..=m {
            if pre[i][j] == k {
                res += 1;
            }
        }
    }
    print!("{res}");
}
