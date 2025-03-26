use std::collections::VecDeque;
use std::io::{read_to_string, stdin};

fn jinu_bfs(r: usize, c: usize, n: usize, m: usize, graph: &Vec<Vec<char>>) -> Vec<Vec<i32>> {
    let dy = vec![-1, 0, 1, 0];
    let dx = vec![0, 1, 0, -1];
    let mut queue = VecDeque::new();
    let mut visited = vec![vec![-1; m]; n];

    let n = n as i32;
    let m = m as i32;

    visited[r][c] = 0;
    queue.push_back((r, c));

    while let Some((y, x)) = queue.pop_front() {
        for i in 0..4 {
            let ny = y as i32 + dy[i];
            let nx = x as i32 + dx[i];

            if ny < 0 || nx < 0 || ny >= n || nx >= m {
                continue;
            }
            let ny = ny as usize;
            let nx = nx as usize;
            if visited[ny][nx] == -1 && graph[ny][nx] != '#' {
                visited[ny][nx] = visited[y][x] + 2;
                queue.push_back((ny, nx));
            }
        }
    }
    visited
}

fn chan_bfs(
    r: usize,
    c: usize,
    n: usize,
    m: usize,
    graph: &Vec<Vec<char>>,
    jinu_visited: Vec<Vec<i32>>,
) -> i32 {
    let dy = vec![-1, 0, 1, 0];
    let dx = vec![0, 1, 0, -1];
    let mut visited = vec![vec![-1; m]; n];
    let mut queue = VecDeque::new();
    queue.push_back((r, c));
    visited[r][c] = 0;

    let n = n as i32;
    let m = m as i32;

    let mut res = if jinu_visited[r][c] != -1 {
        jinu_visited[r][c]
    } else {
        i32::MAX
    };

    while let Some((y, x)) = queue.pop_front() {
        if graph[y][x] == 'T' {
            res = res.min(jinu_visited[y][x] + visited[y][x]);
        }

        for i in 0..4 {
            let ny = y as i32 + dy[i];
            let nx = x as i32 + dx[i];
            if ny < 0 || nx < 0 || ny >= n || nx >= m {
                continue;
            }
            let ny = ny as usize;
            let nx = nx as usize;
            if visited[ny][nx] == -1 && graph[ny][nx] != '#' {
                visited[ny][nx] = visited[y][x] + 1;
                queue.push_back((ny, nx));
            }
        }
    }

    if res != i32::MAX {
        return res;
    }
    -1
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let s: Vec<Vec<char>> = (0..n).map(|_| next().chars().collect()).collect();

    let mut jinu_visited = Vec::new();

    for i in 0..n {
        for j in 0..m {
            if s[i][j] == 'J' {
                jinu_visited = jinu_bfs(i, j, n, m, &s);
            }
        }
    }

    for i in 0..n {
        for j in 0..m {
            if s[i][j] == 'S' {
                print!("{}", chan_bfs(i, j, n, m, &s, jinu_visited));
                return;
            }
        }
    }
}
