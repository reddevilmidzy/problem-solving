use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

const INF: u32 = 1_000_000_000;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let board: Vec<Vec<usize>> = (0..n)
        .map(|_| (0..n).map(|_| next().parse::<usize>().unwrap()).collect())
        .collect();

    let mut idx = vec![(0, 0); n * n + 2];

    let rb: [[(i32, i32); 4]; 2] = [
        [(0, 1), (0, -1), (1, 0), (-1, 0)],
        [(1, 1), (1, -1), (-1, 1), (-1, -1)],
    ];

    for i in 0..n {
        for j in 0..n {
            idx[board[i][j]] = (i, j);
        }
    }

    // dummy
    idx[n * n + 1] = (0, 0);

    let nn = n as i32;
    // y,x,piece_type,idx
    // piece_type, idx, y, x
    let mut visited = vec![vec![vec![vec![INF; n]; n]; n * n + 1]; 3];
    let (st_y, st_x) = idx[1];
    let n_pow = n * n;

    // knight
    visited[0][1][st_y][st_x] = 0;
    // rook
    visited[1][1][st_y][st_x] = 0;
    // bishop
    visited[2][1][st_y][st_x] = 0;

    let mut changed = vec![vec![vec![vec![INF; n]; n]; n * n + 1]; 3];
    // knight
    changed[0][1][st_y][st_x] = 0;
    // rook
    changed[1][1][st_y][st_x] = 0;
    // bishop
    changed[2][1][st_y][st_x] = 0;

    let mut hq = BinaryHeap::new();
    hq.push(Reverse((0, 0, 1, 0, st_y as i32, st_x as i32)));
    hq.push(Reverse((0, 0, 1, 1, st_y as i32, st_x as i32)));
    hq.push(Reverse((0, 0, 1, 2, st_y as i32, st_x as i32)));

    while let Some(Reverse((dist, cnt, i, p, y, x))) = hq.pop() {
        let yy = y as usize;
        let xx = x as usize;

        changed[p][i][yy][xx] = changed[p][i][yy][xx].min(cnt);

        if i >= n_pow {
            continue;
        }

        if p == 0 {
            for (dy, dx) in [
                (2, 1),
                (2, -1),
                (-2, 1),
                (-2, -1),
                (1, 2),
                (1, -2),
                (-1, 2),
                (-1, -2),
            ] {
                let ny = dy + y;
                let nx = dx + x;
                if ny < 0 || nx < 0 || ny >= nn || nx >= nn {
                    continue;
                }
                let ny = ny as usize;
                let nx = nx as usize;
                let ni = if (ny, nx) == idx[i + 1] { i + 1 } else { i };

                // lst is knignt
                if visited[p][ni][ny][nx] > dist + 1 {
                    visited[p][ni][ny][nx] = dist + 1;
                    changed[p][ni][ny][nx] = changed[p][ni][ny][nx].min(cnt);
                    hq.push(Reverse((dist + 1, cnt, ni, p, ny as i32, nx as i32)));
                } else if visited[p][ni][ny][nx] == dist + 1 {
                    changed[p][ni][ny][nx] = changed[p][ni][ny][nx].min(cnt);
                }
            }
        } else {
            for (dy, dx) in rb[p - 1] {
                for nxt in 1..=nn {
                    let ny = dy * nxt + y;
                    let nx = dx * nxt + x;
                    if ny < 0 || nx < 0 || ny >= nn || nx >= nn {
                        break;
                    }
                    let ny = ny as usize;
                    let nx = nx as usize;
                    let ni = if (ny, nx) == idx[i + 1] { i + 1 } else { i };

                    // lst is rook, bishop

                    if visited[p][ni][ny][nx] > dist + 1 {
                        visited[p][ni][ny][nx] = dist + 1;
                        changed[p][ni][ny][nx] = changed[p][ni][ny][nx].min(cnt);
                        hq.push(Reverse((dist + 1, cnt, ni, p, ny as i32, nx as i32)));
                    } else if visited[p][ni][ny][nx] == dist + 1 {
                        changed[p][ni][ny][nx] = changed[p][ni][ny][nx].min(cnt);
                    }
                }
            }
        }

        for np in 0..3 {
            if p == np {
                continue;
            }
            let ni = if (yy, xx) == idx[i + 1] { i + 1 } else { i };

            if visited[np][ni][yy][xx] > dist + 1 {
                visited[np][ni][yy][xx] = dist + 1;
                changed[np][ni][yy][xx] = changed[np][ni][yy][xx].min(cnt + 1);
                hq.push(Reverse((dist + 1, cnt + 1, ni, np, y, x)));
            } else if visited[np][ni][yy][xx] == dist + 1 {
                changed[np][ni][yy][xx] = changed[np][ni][yy][xx].min(cnt + 1);
            }
        }
    }

    let (lst_y, lst_x) = idx[n_pow];

    let mut res = INF;
    let mut ans = INF;
    for i in 0..3 {
        if res > visited[i][n_pow][lst_y][lst_x] {
            res = visited[i][n_pow][lst_y][lst_x];
            ans = changed[i][n_pow][lst_y][lst_x];
        } else if res == visited[i][n_pow][lst_y][lst_x] {
            ans = ans.min(changed[i][n_pow][lst_y][lst_x]);
        }
    }
    print!("{res} {ans}");
}
