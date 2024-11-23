use std::io::{read_to_string, stdin};

fn find_leaf(root: usize, n: usize, graph: &Vec<Vec<usize>>) -> &str {
    let mut stk: Vec<Vec<usize>> = Vec::new();
    stk.push(vec![root, 0]);
    let mut visited: Vec<bool> = vec![false; n + 1];

    visited[root] = true;
    let mut is_child: Vec<bool> = vec![true; n + 1];

    let mut cnt: Vec<i32> = vec![0; n + 1];

    while stk.len() > 0 {
        let cur: Vec<usize> = stk.pop().unwrap();

        let mut has_child = false;

        for nxt in &graph[cur[0]] {
            if *nxt != cur[1] {
                has_child = true;
                cnt[*nxt] = cnt[cur[0]] + 1;
                stk.push(vec![*nxt, cur[0]]);
            }
        }
        if has_child {
            is_child[cur[0]] = false;
        }
    }
    let mut res = 0;

    for i in 1..=n {
        if is_child[i] {
            res += cnt[i];
        }
    }
    if res % 2 == 0 {
        return "No";
    }
    "Yes"
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut graph: Vec<Vec<usize>> = vec![vec![]; n + 1];

    for _ in 0..n - 1 {
        let u: usize = next().parse().unwrap();
        let v: usize = next().parse().unwrap();

        graph[u].push(v);
        graph[v].push(u);
    }

    print!("{}", find_leaf(1, n, &graph));
}
