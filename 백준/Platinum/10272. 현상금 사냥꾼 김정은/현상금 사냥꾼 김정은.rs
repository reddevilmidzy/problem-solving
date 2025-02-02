use std::fmt::Write;
use std::io::{read_to_string, stdin};

#[derive(Debug, Clone, Copy)]
struct Point {
    y: u32,
    x: u32,
}

trait Dist {
    fn calc_dist(&self, point: Point) -> f64;
}

impl Dist for Point {
    fn calc_dist(&self, point: Point) -> f64 {
        ((self.y.abs_diff(point.y).pow(2) + self.x.abs_diff(point.x).pow(2)) as f64).sqrt()
    }
}
fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut stdout = String::new();

    let t: usize = next().parse().unwrap();
    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        let nums: Vec<Point> = (0..n)
            .map(|_| Point {
                x: next().parse::<u32>().unwrap(),
                y: next().parse::<u32>().unwrap(),
            })
            .collect();
        writeln!(stdout, "{}", solve(n, nums)).unwrap();
    }
    print!("{}", stdout);
}

fn solve(n: usize, nums: Vec<Point>) -> f64 {
    let mut dp = vec![vec![1_000_000_f64; n + 1]; n + 1];
    // dp[i][j] i까지 상승 j 까지 하강

    dp[0][0] = 0.0;
    dp[1][0] = 0.0;
    dp[0][1] = 0.0;

    for i in 0..=n {
        for j in 0..=n {
            if i == j {
                continue;
            }
            let nxt = i.max(j) + 1;
            if nxt > n {
                continue;
            }
            dp[nxt][j] = dp[nxt][j].min(
                dp[i][j]
                    + if i != 0 {
                        nums[i - 1].calc_dist(nums[nxt - 1])
                    } else {
                        nums[0].calc_dist(nums[nxt - 1])
                    },
            );
            dp[i][nxt] = dp[i][nxt].min(
                dp[i][j]
                    + if j != 0 {
                        nums[j - 1].calc_dist(nums[nxt - 1])
                    } else {
                        nums[0].calc_dist(nums[nxt - 1])
                    },
            );
        }
    }

    let mut res = f64::MAX;

    for i in 1..=n {
        res = res.min(dp[n][i] + nums[i - 1].calc_dist(nums[n - 1]));
    }
    res
}
