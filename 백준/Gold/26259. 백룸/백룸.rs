use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let a: Vec<Vec<i32>> = (0..n)
        .map(|_| (0..m).map(|_| next().parse::<i32>().unwrap()).collect())
        .collect();

    let (y1, x1, y2, x2): (usize, usize, usize, usize) = (
        next().parse().unwrap(),
        next().parse().unwrap(),
        next().parse().unwrap(),
        next().parse().unwrap(),
    );

    let no_wall = (y1, x1) == (y2, x2);
    let hori = !no_wall && (y1 == y2);
    let vert = !no_wall && (x1 == x2);

    let inf = i32::MIN;
    let mut dp = vec![vec![inf; m]; n];
    dp[0][0] = a[0][0];

    for y in 0..n {
        for x in 0..m {
            if y > 0
                && dp[y - 1][x] != inf
                && !(hori && y == y1 && x1.min(x2) <= x && x < x1.max(x2))
            {
                dp[y][x] = dp[y][x].max(dp[y - 1][x] + a[y][x]);
            }
            if x > 0
                && dp[y][x - 1] != inf
                && !(vert && x == x1 && y1.min(y2) <= y && y < y1.max(y2))
            {
                dp[y][x] = dp[y][x].max(dp[y][x - 1] + a[y][x]);
            }
        }
    }

    if (y1 == 0 && y2 == n && (1 <= x1 && x1 < m)) || (x1 == 0 && x2 == m && (1 <= y1 && y1 < n)) {
        print!("Entity");
    } else if (dp[n - 1][m - 1]) == inf {
        print!("Entity");
    } else {
        print!("{}", dp[n - 1][m - 1]);
    }
}
