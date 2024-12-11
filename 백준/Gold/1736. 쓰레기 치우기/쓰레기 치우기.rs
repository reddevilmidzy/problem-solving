use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut board: Vec<Vec<i32>> = (0..n).map(|_| (0..m).map(|_| next().parse::<i32>().unwrap()).collect()).collect();
    // 생각한 전략은 위에서 최대 j 보다 큰 것들은 처리할 수 있음

    let mut res = 0;
    for i in 0..n {
        // 거꾸로 가면서 시작할 거임
        for j in (0..m).rev() {
            if board[i][j] == 1 {
                res += 1;
                let mut lst_x = j;

                for ny in (i + 1)..n {
                    let mut tmp_x = lst_x;
                    for nx in lst_x..m {
                        if board[ny][nx] == 1 {
                            board[ny][nx] = 0;
                            tmp_x = nx;
                        }
                    }
                    // 마지막 1으로 변환
                    lst_x = tmp_x;
                }
                break;
            }
        }
    }
    print!("{res}");
}
