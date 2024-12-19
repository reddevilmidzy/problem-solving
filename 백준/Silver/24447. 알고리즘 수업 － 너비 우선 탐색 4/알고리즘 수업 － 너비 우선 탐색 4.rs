use std::collections::VecDeque;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let st: usize = next().parse().unwrap();

    let mut graph = vec![Vec::new(); n + 1];
    for _ in 0..m {
        let (u, v): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        graph[u].push(v);
        graph[v].push(u);
    }

    for i in 0..=n {
        graph[i].sort();
    }

    let mut res: u64 = 0;
    let mut visited: Vec<bool> = vec![false; n + 1];
    visited[st] = true;

    let mut queue = VecDeque::new();
    queue.push_back((st, 0));

    let mut cnt = 1;
    while !queue.is_empty() {
        let (cur, depth) = queue.pop_front().unwrap();
        res += cnt * depth;
        cnt += 1;
        for nxt in &graph[cur] {
            if !visited[*nxt] {
                visited[*nxt] = true;
                queue.push_back((*nxt, depth + 1));
            }
        }
    }

    print!("{res}");
}
