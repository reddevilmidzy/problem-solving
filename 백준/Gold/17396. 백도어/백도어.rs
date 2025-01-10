use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

const INF: u64 = u64::MAX;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let can_go: Vec<bool> = (0..n).map(|x| (next() == "0" || x == n - 1)).collect();


    let mut graph: Vec<Vec<(usize, u64)>> = vec![Vec::new(); n];
    for _ in 0..m {
        let (u, v, w): (usize, usize, u64) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );

        if !can_go[u] || !can_go[v] {
            continue;
        }
        graph[u].push((v, w));
        graph[v].push((u, w));
    }

    let mut distance = vec![INF; n];
    distance[0] = 0;
    let mut hq = BinaryHeap::new();
    hq.push((Reverse(distance[0]), 0usize));

    while let Some((dist, cur)) = hq.pop() {
        if distance[cur] < dist.0 {
            continue;
        }

        for (nxt, cost) in &graph[cur] {
            if distance[cur] + cost < distance[*nxt] {
                distance[*nxt] = distance[cur] + cost;
                hq.push((Reverse(distance[*nxt]), *nxt));
            }
        }
    }

    if distance[n - 1] != INF {
        print!("{}", distance[n - 1]);
    } else {
        print!("-1");
    }
}
