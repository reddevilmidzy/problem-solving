use std::io::{read_to_string, stdin};

fn dfs(visited: &mut Vec<bool>, graph: &Vec<Vec<usize>>, cur: usize) -> u32 {
    let mut tot = 1;
    visited[cur] = true;

    for &nxt in &graph[cur] {
        if !visited[nxt] {
            tot += dfs(visited, graph, nxt);
        }
    }

    tot
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut graph = vec![Vec::new(); n + 1];
    for _ in 0..n - 1 {
        let (u, v): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        graph[u].push(v);
        graph[v].push(u);
    }

    let (a, b, x): (usize, usize, usize) = (
        next().parse().unwrap(),
        next().parse().unwrap(),
        next().parse().unwrap(),
    );

    // a==b==x 는 전부다 될 수 있음
    // a==b != x 는 x 위에 있는 녀석들 모두
    // (a,b) 와 x 경로 사이에 있냐

    let mut visited = vec![false; n + 1];
    visited[x] = true;
    let mut meet_a = a == x;
    let mut meet_b = b == x;

    let mut res = 1;
    for &child in &graph[x] {
        let cnt = dfs(&mut visited, &graph, child);
        if visited[a] && !meet_a && visited[b] && !meet_b {
            meet_a = true;
            meet_b = true;
        } else if visited[a] && !meet_a {
            meet_a = true;
        } else if visited[b] && !meet_b {
            meet_b = true;
        } else {
            res += cnt;
        }
    }

    print!("{res}");
}
