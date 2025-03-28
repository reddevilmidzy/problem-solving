use std::collections::VecDeque;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut graph = vec![Vec::new(); n + m + 1];
    for i in 0..m {
        for _ in 0..k {
            let cur: usize = next().parse().unwrap();
            graph[cur].push(i + n + 1);
            graph[i + n + 1].push(cur);
        }
    }

    let mut queue = VecDeque::new();
    queue.push_back(1);
    let mut visited = vec![i32::MAX; n + m + 1];
    visited[1] = 1;

    while let Some(cur) = queue.pop_front() {
        if cur == n {
            print!("{}", visited[cur]);
            return;
        }
        for &nxt in &graph[cur] {
            if nxt > n && visited[nxt] > visited[cur] {
                visited[nxt] = visited[cur];
                queue.push_back(nxt);
            } else if nxt <= n && visited[nxt] > visited[cur] + 1 {
                visited[nxt] = visited[cur] + 1;
                queue.push_back(nxt);
            }
        }
    }
    print!("-1");
}
