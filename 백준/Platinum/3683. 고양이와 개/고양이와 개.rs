use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn dfs(
    x: usize,
    visited: &mut Vec<bool>,
    graph: &Vec<Vec<usize>>,
    selected: &mut Vec<i32>,
) -> bool {
    if visited[x] {
        return false;
    }
    visited[x] = true;

    for y in &graph[x] {
        if selected[*y] == -1 || dfs(selected[*y] as usize, visited, graph, selected) {
            selected[*y] = x as i32;
            return true;
        }
    }

    false
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut res = String::new();

    let t: u8 = next().parse().unwrap();
    for _ in 0..t {
        let (_c, _d, v): (usize, usize, usize) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );

        let votes: Vec<(&str, &str)> = (0..v).map(|_| (next(), next())).collect();

        let mut selected = vec![-1; v];
        let mut graph = vec![Vec::new(); v];

        for i in 0..v {
            for j in 0..v {
                if votes[i].0 == votes[j].1 || votes[j].0 == votes[i].1 {
                    if votes[i].0.starts_with("C") {
                        graph[i].push(j);
                    } else {
                        graph[j].push(i);
                    }
                }
            }
        }

        let mut cnt = 0;
        for x in 0..v {
            let mut visited = vec![false; v];
            if dfs(x, &mut visited, &graph, &mut selected) {
                cnt += 1;
            }
        }

        writeln!(res, "{}", v - cnt).unwrap();
    }
    print!("{res}");
}
