use std::fmt::Write;
use std::io::{read_to_string, stdin};

const M: usize = 8;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next();

    let mut res = String::new();

    while let Some(s) = next() {
        let board = generate(s.to_string());
        writeln!(res, "{}", solve(board)).unwrap();
    }
    print!("{res}");
}

fn generate(s: String) -> Vec<Vec<char>> {
    let mut res = vec![vec![' '; M]; M];

    let lines: Vec<&str> = s.split("/").collect();

    let mut i = 0;
    for line in lines {
        let mut j = 0;
        for c in line.chars() {
            if c.is_numeric() {
                let tmp: usize = c.to_digit(10).unwrap() as usize;
                j += tmp;
                continue;
            }
            res[i][j] = c;
            j += 1;
        }
        i += 1;
    }

    res
}

fn solve(board: Vec<Vec<char>>) -> u32 {
    let mut res = 0;
    let mut visited = vec![vec![false; M]; M];

    for i in 0..M {
        for j in 0..M {
            if board[i][j] == ' ' {
                continue;
            }
            visited[i][j] = true;
            if board[i][j] == 'r' || board[i][j] == 'R' {
                rook(i, j, &board, &mut visited);
            } else if board[i][j] == 'b' || board[i][j] == 'B' {
                bishop(i, j, &board, &mut visited);
            } else if board[i][j] == 'n' || board[i][j] == 'N' {
                knight(i, j, &mut visited);
            } else if board[i][j] == 'q' || board[i][j] == 'Q' {
                rook(i, j, &board, &mut visited);
                bishop(i, j, &board, &mut visited);
            } else if board[i][j] == 'k' || board[i][j] == 'K' {
                king(i, j, &mut visited);
            } else if board[i][j] == 'p' {
                // todo 블랙
                pawn(i, j, &mut visited, 1);
            } else if board[i][j] == 'P' {
                // todo 화이트
                pawn(i, j, &mut visited, -1);
            }
        }
    }

    for i in 0..M {
        for j in 0..M {
            if !visited[i][j] {
                res += 1;
            }
        }
    }
    res
}

fn pawn(r: usize, c: usize, visited: &mut Vec<Vec<bool>>, way: i32) {
    let d = vec![(way, -1), (way, 1)];
    check(r, c, visited, d);
}

fn king(r: usize, c: usize, visited: &mut Vec<Vec<bool>>) {
    let d = vec![(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)];
    check(r, c, visited, d);
}

fn check(r: usize, c: usize, visited: &mut Vec<Vec<bool>>, d: Vec<(i32, i32)>) {
    let m = 8;
    for (y, x) in d {
        let ny = r as i32 + y;
        let nx = c as i32 + x;

        if ny < 0 || nx < 0 || ny >= m || nx >= m {
            continue;
        }
        let ny = ny as usize;
        let nx = nx as usize;
        visited[ny][nx] = true;
    }
}

fn knight(r: usize, c: usize, visited: &mut Vec<Vec<bool>>) {
    let d = vec![
        (2, 1),
        (-2, 1),
        (2, -1),
        (-2, -1),
        (1, 2),
        (-1, 2),
        (1, -2),
        (-1, -2),
    ];
    check(r, c, visited, d);
}

fn rook(r: usize, c: usize, board: &Vec<Vec<char>>, visited: &mut Vec<Vec<bool>>) {
    let mut i = r + 1;
    while i < M {
        if board[i][c] != ' ' {
            break;
        }
        visited[i][c] = true;
        i += 1;
    }

    let mut i = r as i32 - 1;
    while i >= 0 {
        if board[i as usize][c] != ' ' {
            break;
        }
        visited[i as usize][c] = true;
        i -= 1;
    }

    let mut j = c + 1;
    while j < M {
        if board[r][j] != ' ' {
            break;
        }
        visited[r][j] = true;
        j += 1;
    }

    let mut j = c as i32 - 1;
    while j >= 0 {
        if board[r][j as usize] != ' ' {
            break;
        }
        visited[r][j as usize] = true;
        j -= 1;
    }
}

fn bishop(r: usize, c: usize, board: &Vec<Vec<char>>, visited: &mut Vec<Vec<bool>>) {
    let mut i = r + 1;
    let mut j = c + 1;
    while i < M && j < M {
        if board[i][j] != ' ' {
            break;
        }
        visited[i][j] = true;
        i += 1;
        j += 1;
    }

    let mut i = r + 1;
    let mut j = c as i32 - 1;
    while i < M && j >= 0 {
        if board[i][j as usize] != ' ' {
            break;
        }
        visited[i][j as usize] = true;
        i += 1;
        j -= 1
    }

    let mut i = r as i32 - 1;
    let mut j = c + 1;
    while i >= 0 && j < M {
        if board[i as usize][j] != ' ' {
            break;
        }
        visited[i as usize][j] = true;
        i -= 1;
        j += 1;
    }

    let mut i = r as i32 - 1;
    let mut j = c as i32 - 1;
    while i >= 0 && j >= 0 {
        if board[i as usize][j as usize] != ' ' {
            break;
        }
        visited[i as usize][j as usize] = true;
        i -= 1;
        j -= 1;
    }
}

#[test]
fn tmp() {
    let res = generate("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR".to_string());
    // let res = generate("5k1r/2q3p1/p3p2p/1B3p1Q/n4P2/6P1/bbP2N1P/1K1RR3".to_string());
    println!("{:?}", solve(res));
}
