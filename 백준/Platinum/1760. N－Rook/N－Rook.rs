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
    let mut r_cnt = 1;

    for i in 0..n {
        let mut cur = None;

        for j in 0..m {
            if board[i][j] == 2 {
                cur = None;
            } else {
                if cur.is_none() {
                    cur = Some(r_cnt);
                    r_cnt += 1;
                }
                row[i][j] = cur.unwrap();
            }
        }
    }

    let mut col = vec![vec![0; m]; n];
    let mut c_cnt = 1;
    for j in 0..m {
        let mut cur = None;
        for i in 0..n {
            if board[i][j] == 2{
                cur = None;
            } else {
                if cur.is_none() {
                    cur = Some(c_cnt);
                    c_cnt += 1;
                }
                col[i][j] = cur.unwrap();
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

    // println!("{:?}", row);
    // println!("{:?}", col);
    print!("{res}");
}
