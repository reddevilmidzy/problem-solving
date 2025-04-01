use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap, HashSet};
use std::io::{read_to_string, stdin};

fn dijkstra(graph: &Vec<Vec<(usize, u64)>>, st: usize, n: usize) -> Vec<u64> {
    let inf = u64::MAX;
    let mut distance = vec![inf; n + 1];
    let mut hq = BinaryHeap::new();
    distance[st] = 0;
    hq.push(Reverse((distance[st], st)));
    // 데익 한번 돌려서 최단 경로 구한다음 그 경로 없애고, 다시 데익

    while let Some(Reverse((dist, cur))) = hq.pop() {
        if distance[cur] < dist {
            continue;
        }

        for &(nxt, cost) in &graph[cur] {
            if dist + cost < distance[nxt] {
                distance[nxt] = dist + cost;
                hq.push(Reverse((distance[nxt], nxt)));
            }
        }
    }

    distance
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let mut graph = vec![Vec::new(); n + 1];
    let mut edges = HashMap::new();

    for _ in 0..m {
        let (u, v, w): (usize, usize, u64) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );
        graph[u].push((v, w));
        graph[v].push((u, w));
        edges.insert((u, v), w);
        edges.insert((v, u), w);
    }

    let inf = u64::MAX;
    let mut distance = vec![inf; n + 1];
    let mut hq = BinaryHeap::new();
    distance[1] = 0;
    hq.push(Reverse((distance[1], 1)));
    let mut route = vec![0; n + 1];
    // 데익 한번 돌려서 최단 경로 구한다음 그 경로 없애고, 다시 데익

    while let Some(Reverse((dist, cur))) = hq.pop() {
        if distance[cur] < dist {
            continue;
        }

        for &(nxt, cost) in &graph[cur] {
            if dist + cost < distance[nxt] {
                route[nxt] = cur;
                distance[nxt] = dist + cost;
                hq.push(Reverse((distance[nxt], nxt)));
            }
        }
    }

    let mut used = HashSet::new();

    let mut cur = n;
    let mut min_edge = inf;

    while cur != 1 {
        min_edge = min_edge.min(*edges.get(&(cur, route[cur])).unwrap());
        used.insert((cur, route[cur]));
        cur = route[cur];
    }

    let mut sec = vec![inf; n + 1];
    sec[1] = 0;

    hq.push(Reverse((sec[1], 1)));
    while let Some(Reverse((dist, cur))) = hq.pop() {
        if sec[cur] < dist {
            continue;
        }
        for &(nxt, cost) in &graph[cur] {
            if dist + cost < sec[nxt] {
                if used.contains(&(nxt, cur)) || used.contains(&(cur, nxt)) {
                    if dist + cost * 3 < sec[nxt] {
                        sec[nxt] = dist + cost * 3;
                        hq.push(Reverse((sec[nxt], nxt)));
                    }
                } else {
                    sec[nxt] = dist + cost;
                    hq.push(Reverse((sec[nxt], nxt)));
                }
            }
        }
    }

    let go = dijkstra(&graph, 1, n);
    let back = dijkstra(&graph, n, n);

    let mut res = inf;
    res = res.min(sec[n]);
    res = res.min(distance[n] + min_edge * 2);

    for i in 2..n - 1 {
        if go[i] + back[i] == go[n] {
            continue;
        }
        res = res.min(go[i] + back[i]);
    }

    print!("{res}");
}
