use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn dfs(
    cur: usize,
    graph: &Vec<Vec<usize>>,
    order: &mut Vec<u32>,
    parent: &mut Vec<usize>,
    low: &mut Vec<u32>,
    res: &mut HashSet<usize>,
    t: &mut u32,
) {
    order[cur] = *t;
    *t += 1;
    low[cur] = order[cur];
    let mut child = 0;

    for &nxt in &graph[cur] {
        if nxt == parent[cur] {
            continue;
        }
        if order[nxt] == 0 {
            parent[nxt] = cur;
            child += 1;
            dfs(nxt, graph, order, parent, low, res, t);

            if (parent[cur] == 0 && child > 1) || (parent[cur] != 0 && low[nxt] >= order[cur]) {
                res.insert(cur);
            }

            low[cur] = low[cur].min(low[nxt]);
        } else {
            low[cur] = low[cur].min(order[nxt]);
        }
    }
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let mut graph = vec![Vec::new(); n + 1];
    for _ in 0..m {
        let u: usize = next().parse().unwrap();
        let v: usize = next().parse().unwrap();

        graph[u].push(v);
        graph[v].push(u);
    }

    let mut order = vec![0; n + 1];
    let mut parent = vec![0; n + 1];
    let mut low = vec![0; n + 1];
    let mut res = HashSet::new();
    let mut t = 1;

    for i in 1..=n {
        if order[i] == 0 {
            dfs(
                i,
                &graph,
                &mut order,
                &mut parent,
                &mut low,
                &mut res,
                &mut t,
            );
        }
    }

    println!("{}", res.len());
    let mut res = res.into_iter().collect::<Vec<_>>();
    res.sort();
    for i in res {
        print!("{i} ");
    }
}
