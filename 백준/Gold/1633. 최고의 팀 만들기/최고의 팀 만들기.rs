use std::io::{read_to_string, stdin};

struct Player {
    white: u32,
    black: u32,
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next();

    let mut candy = Vec::new();
    while let Some(white) = next() {
        let white = white.parse::<u32>().unwrap();
        let black = next().unwrap().parse::<u32>().unwrap();
        candy.push(Player { white, black });
    }
    print!("{}", solve(candy));
}

fn solve(candy: Vec<Player>) -> u32 {
    let m = 15;
    let n = candy.len();
    let mut dp = vec![vec![vec![0; m + 1]; m + 1]; n + 1];

    dp[1][0][1] = candy[0].black;
    dp[1][1][0] = candy[0].white;
    let mut res = 0;

    for i in 1..=n {
        for white in 0..=m {
            for black in 0..=m {
                if white + black > i {
                    break;
                }
                dp[i][white][black] = dp[i][white][black].max(dp[i - 1][white][black]);

                if white > 0 {
                    dp[i][white][black] =
                        dp[i][white][black].max(dp[i - 1][white - 1][black] + candy[i - 1].white);
                }
                if black > 0 {
                    dp[i][white][black] =
                        dp[i][white][black].max(dp[i - 1][white][black - 1] + candy[i - 1].black);
                }
            }
        }
        res = res.max(dp[i][m][m]);
    }

    res
}
