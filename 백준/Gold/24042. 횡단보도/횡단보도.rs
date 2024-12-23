use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut graph = vec![Vec::new(); n + 1];
    for i in 0..m {
        let u: usize = next().parse().unwrap();
        let v: usize = next().parse().unwrap();
        graph[u].push((v, i));
        graph[v].push((u, i));
    }

    let mut hq = BinaryHeap::new();
    let mut distance = vec![usize::MAX; n + 1];

    let st = 1;

    distance[st] = 0;
    hq.push((Reverse(distance[st]), st));

    while !hq.is_empty() {
        let (dist, cur) = hq.pop().unwrap();

        if dist.0 > distance[cur] {
            continue;
        }

        for (nxt, per) in &graph[cur] {
            // 기다리는 시간
            let cur_per = dist.0 % m;
            let left_time = if cur_per <= *per {
                per - cur_per
            } else {
                per + (m - cur_per)
            };

            if dist.0 + left_time + 1 < distance[*nxt] {
                distance[*nxt] = dist.0 + left_time + 1;
                hq.push((Reverse(distance[*nxt]), *nxt));
            }
        }
    }

    print!("{:?}", distance[n]);
}
