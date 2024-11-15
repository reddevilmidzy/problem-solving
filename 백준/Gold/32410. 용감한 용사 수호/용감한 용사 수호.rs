use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let first_line = input.next().unwrap().unwrap();
    let mut iter = first_line.split_whitespace();

    let k: usize = 300;
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();
    let x: usize = iter.next().unwrap().parse().unwrap();
    let y: usize = iter.next().unwrap().parse().unwrap();

    let mut dp: Vec<Vec<i32>> = vec![vec![100_000; k + 1]; k + 1];
    dp[x][y] = 0;

    for _ in 0..n {
        let line = input.next().unwrap().unwrap();
        let mut iter = line.split_whitespace();
        let u: usize = iter.next().unwrap().parse().unwrap();
        let v: usize = iter.next().unwrap().parse().unwrap();

        for i in (0..=k).rev() {
            for j in (0..=k).rev() {
                let nu = k.min(i + u);
                let nv = k.min(j + v);
                dp[nu][nv] = dp[nu][nv].min(dp[i][j] + 1);
            }
        }
    }

    let cnt: usize = input.next().unwrap().unwrap().parse().unwrap();
    let mut knap: Vec<Vec<i32>> = vec![vec![0; k + 1]; k + 1];

    for _ in 0..cnt {
        let line = input.next().unwrap().unwrap();
        let mut iter = line.split_whitespace();
        let u: usize = iter.next().unwrap().parse().unwrap();
        let v: usize = iter.next().unwrap().parse().unwrap();

        knap[u][v] += 1;
    }

    for i in 0..=k {
        let mut x = 0;
        for j in 0..=k {
            x += knap[i][j];
            knap[i][j] = x;
        }
    }

    for j in 0..=k {
        let mut x = 0;
        for i in 0..=k {
            x += knap[i][j];
            knap[i][j] = x;
        }
    }

    let mut res = 0;
    for i in 0..=k {
        for j in 0..=k {
            if dp[i][j] <= m as i32 {
                res = res.max(knap[i][j]);
            }
        }
    }
    print!("{res}");
}