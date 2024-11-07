use std::collections::VecDeque;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().lines();

    let lines = input.next().unwrap().unwrap();
    let mut iter = lines.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();
    let d: usize = iter.next().unwrap().parse().unwrap();

    let mut board: Vec<Vec<char>> = Vec::new();
    for _ in 0..n {
        let line = input.next().unwrap().unwrap();
        board.push(line.chars().collect());
    }

    let mut bomb = vec![vec![i32::MAX; m]; n];
    bomb[0][0] = 0;

    let mut queue = VecDeque::new();
    queue.push_back((0, 0, 0)); // cnt, y, x

    while let Some((cnt, y, x)) = queue.pop_front() {
        if y == n - 1 && x == m - 1 {
            break;
        }
        if bomb[y][x] < cnt {
            continue;
        }

        for (dy, dx) in &[(0, -1), (0, 1), (1, 0), (-1, 0)] {
            let ny = y as isize + dy;
            let nx = x as isize + dx;

            if ny < 0 || nx < 0 || ny >= n as isize || nx >= m as isize {
                continue;
            }
            let ny = ny as usize;
            let nx = nx as usize;

            if board[ny][nx] == '.' && bomb[y][x] < bomb[ny][nx] {
                bomb[ny][nx] = bomb[y][x];
                queue.push_front((bomb[ny][nx], ny, nx));
            }
        }

        for (ddy, ddx) in &[(0, d as isize), (0, -(d as isize)), (-(d as isize), 0), (d as isize, 0)] {
            for i in -((d as isize) - 1)..d as isize {
                let ny = y as isize + ddy + if *ddy == 0 { i } else { 0 };
                let nx = x as isize + ddx + if *ddx == 0 { i } else { 0 };

                let ny = ny.max(0).min(n as isize - 1) as usize;
                let nx = nx.max(0).min(m as isize - 1) as usize;

                if bomb[y][x] + 1 < bomb[ny][nx] {
                    bomb[ny][nx] = bomb[y][x] + 1;
                    queue.push_back((bomb[ny][nx], ny, nx));
                }
            }
        }
    }

    print!("{}", bomb[n - 1][m - 1]);
}