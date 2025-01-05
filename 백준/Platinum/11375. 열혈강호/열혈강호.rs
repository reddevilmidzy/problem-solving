use std::io::{read_to_string, stdin};

fn dfs(visited: &mut Vec<bool>, selected: &mut Vec<i32>, graph: &Vec<Vec<usize>>, x: usize) -> bool {
    if visited[x] {
        return false;
    }
    visited[x] = true;

    for y in &graph[x] {
        if selected[*y] == -1 {
            selected[*y] = x as i32;
            return true;
        }
    }
    for y in &graph[x] {
        if selected[*y] == -1 || dfs(visited, selected, graph, selected[*y] as usize) {
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

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut graph = Vec::new();
    for _ in 0..n {
        let k: usize = next().parse().unwrap();
        let tmp: Vec<usize> = (0..k).map(|x| next().parse::<usize>().unwrap() - 1).collect();
        graph.push(tmp);
    }

    let mut selected = vec![-1; m];
    let mut res = 0;
    let mv = n.min(m);
    for x in 0..n {
        let mut visited = vec![false; n];
        if dfs(&mut visited, &mut selected, &graph, x) {
            res += 1;
        }
        if mv == res {
            break;
        }
    }
    print!("{res}");
}
