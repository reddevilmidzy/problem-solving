use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let m: usize = next().parse().unwrap();
    let n: usize = next().parse().unwrap();

    let board: Vec<Vec<u8>> = (0..n)
        .map(|_| (0..m).map(|_| next().parse::<u8>().unwrap()).collect())
        .collect();
    let mut can = vec![vec![false; m]; n];
    can[0][0] = true;

    for i in 0..n {
        for j in 0..m {
            if (i + j) == 0 {
                continue;
            } else if i == 0 {
                can[i][j] = can[i][j - 1];
            } else if j == 0 {
                can[i][j] = can[i - 1][j];
            } else {
                can[i][j] = can[i][j - 1] || can[i - 1][j];
            }
            can[i][j] = can[i][j] && (board[i][j] == 1);
        }
    }

    let res = if can[n - 1][m - 1] { "Yes" } else { "No" };
    print!("{res}");
}
