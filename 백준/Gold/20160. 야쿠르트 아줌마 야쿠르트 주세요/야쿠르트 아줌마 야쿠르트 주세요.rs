use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut edges = HashMap::new();

    for _ in 0..m {
        let (u, v, w): (usize, usize, u32) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );
        let min_v = u.min(v);
        let max_v = u.max(v);

        if !edges.contains_key(&(min_v, max_v)) {
            edges.insert((min_v, max_v), w);
        } else {
            let val = *edges.get(&(min_v, max_v)).unwrap();
            edges.insert((min_v, max_v), val.min(w));
        }
    }

    let yogurt: Vec<usize> = (0..10).map(|_| next().parse().unwrap()).collect();
    let st: usize = next().parse().unwrap();
    let mut graph = vec![Vec::new(); n + 1];

    for &(u, v) in edges.keys() {
        let w = *edges.get(&(u, v)).unwrap();
        graph[u].push((v, w));
        graph[v].push((u, w));
    }
    let me = dijkstra(st, n, &graph);
    let mut res = Vec::new();

    let mut cur = yogurt[0];
    let mut time = 0;

    if cur == st {
        res.push(cur);
    }

    for i in 1..10 {
        let dist = dijkstra(cur, n, &graph);
        // println!("cur = {i}, dist = {:?}", dist);

        if dist[yogurt[i]] != u32::MAX { // 도달 가능
            time += dist[yogurt[i]];
            if me[yogurt[i]] <= time {
                res.push(yogurt[i]);
            }
            cur = yogurt[i];
        }

    }

    res.sort();
    if !res.is_empty() {
        print!("{}", res[0]);
    } else {
        print!("-1");
    }
}

fn dijkstra(st: usize, n: usize, graph: &Vec<Vec<(usize, u32)>>) -> Vec<u32> {
    let inf = u32::MAX;
    let mut distance = vec![inf; n + 1];

    distance[st] = 0;
    let mut hq = BinaryHeap::new();
    hq.push((Reverse(distance[st]), st));

    while let Some((dist, cur)) = hq.pop() {
        if distance[cur] < dist.0 {
            continue;
        }

        for &(nxt, cost) in &graph[cur] {
            if distance[cur] + cost < distance[nxt] {
                distance[nxt] = distance[cur] + cost;
                hq.push((Reverse(distance[nxt]), nxt));
            }
        }
    }

    distance
}
