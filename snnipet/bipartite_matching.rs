use std::io::{read_to_string, stdin};

fn dfs(
    x: usize,
    graph: &Vec<Vec<usize>>,
    visited: &mut Vec<bool>,
    selected: &mut Vec<i32>,
) -> bool {
    if visited[x] {
        return false;
    }
    visited[x] = true;

    for &y in &graph[x] {
        if selected[y] == -1 || dfs(selected[y] as usize, graph, visited, selected) {
            selected[y] = x as i32;
            return true;
        }
    }

    false
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let board: Vec<Vec<u32>> = (0..n)
        .map(|_| (0..m).map(|_| next().parse::<u32>().unwrap()).collect())
        .collect();

    let mut row = vec![vec![0; m]; n];
    let mut col = vec![vec![0; m]; n];

    let mut r_cnt = 1;
    let mut c_cnt = 1;

    for i in 0..n {
        for j in 0..m {
            if board[i][j] == 0 {
                row[i][j] = r_cnt;
                if j == m - 1 || board[i][j + 1] == 2 {
                    r_cnt += 1;
                }
            }
        }
    }

    for j in 0..m {
        for i in 0..n {
            if board[i][j] == 0 {
                col[i][j] = c_cnt;
                if i == n - 1 || board[i + 1][j] == 2 {
                    c_cnt += 1;
                }
            }
        }
    }

    let mut graph = vec![Vec::new(); r_cnt + 1];
    for i in 0..n {
        for j in 0..m {
            if board[i][j] == 0 {
                graph[row[i][j]].push(col[i][j]);
            }
        }
    }

    let mut selected = vec![-1; c_cnt + 1];
    let mut res = 0;

    for i in 1..=r_cnt {
        let mut visited = vec![false; r_cnt + 1];
        if dfs(i, &graph, &mut visited, &mut selected) {
            res += 1;
        }
    }

    print!("{res}");
}
