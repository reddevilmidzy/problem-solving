use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let a: usize = next().parse().unwrap();
    let b: usize = next().parse().unwrap();

    let mut board = vec![vec![0u8; m]; n];
    let mut items = Vec::with_capacity(a);
    for _ in 0..a {
        let (u, v): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        board[u - 1][v - 1] = 1;
        items.push((u - 1, v - 1));
    }
    for _ in 0..b {
        let (u, v): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        board[u - 1][v - 1] = 2;
    }

    let start = (0, 0);
    let end = (n - 1, m - 1);

    items.sort();

    let mut route = Vec::with_capacity(items.len() + 2);
    route.push(start);
    for &pt in &items {
        route.push(pt);
    }
    route.push(end);

    let mut ans = 1;
    for seg in 0..(route.len() - 1) {
        let (sx, sy) = route[seg];
        let (ex, ey) = route[seg + 1];
        if ex < sx || ey < sy {
            println!("0");
            return;
        }
        let ways = count_paths(&board, sx, sy, ex, ey);
        if ways == 0 {
            println!("0");
            return;
        }
        ans *= ways;
    }
    println!("{}", ans);
}

fn count_paths(board: &Vec<Vec<u8>>, sx: usize, sy: usize, ex: usize, ey: usize) -> u32 {
    let height = ex - sx + 1;
    let width = ey - sy + 1;
    let mut dp = vec![vec![0u32; width]; height];

    if board[sx][sy] == 2 {
        return 0;
    }
    dp[0][0] = 1;
    for i in 0..height {
        for j in 0..width {
            let cell = board[sx + i][sy + j];
            if cell == 2 {
                dp[i][j] = 0;
                continue;
            }
            if i > 0 {
                dp[i][j] += dp[i - 1][j];
            }
            if j > 0 {
                dp[i][j] += dp[i][j - 1];
            }
        }
    }
    dp[height - 1][width - 1]
}
