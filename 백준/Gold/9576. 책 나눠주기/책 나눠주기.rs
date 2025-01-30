use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn dfs(
    visited: &mut Vec<bool>,
    selected: &mut Vec<i32>,
    graph: &Vec<(usize, usize)>,
    x: usize,
) -> bool {
    if visited[x] {
        return false;
    }
    visited[x] = true;

    for y in graph[x].0..=graph[x].1 {
        if selected[y] == -1 {
            selected[y] = x as i32;
            return true;
        }
    }

    for y in graph[x].0..=graph[x].1 {
        if selected[y] == -1 || dfs(visited, selected, graph, selected[y] as usize) {
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
    let mut stdout = String::new();

    let t: usize = next().parse().unwrap();

    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        let m: usize = next().parse().unwrap();

        let mut graph = vec![(0, 0); m];
        for i in 0..m {
            let (u, v): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
            graph[i] = (u-1, v-1);
        }

        writeln!(stdout, "{}", solve(n, m, graph)).unwrap();
    }

    print!("{}", stdout);
}

fn solve(n: usize, m: usize, graph: Vec<(usize, usize)>) -> u32 {
    let mut selected = vec![-1; n];
    let mut res = 0;
    for x in 0..m {
        let mut visited = vec![false; m];
        if dfs(&mut visited, &mut selected, &graph, x) {
            res += 1;
        }
    }
    res
}
