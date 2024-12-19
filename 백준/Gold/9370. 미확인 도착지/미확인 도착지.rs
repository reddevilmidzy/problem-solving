use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

fn dijkstra(st: usize, n: usize, g: usize, h: usize, graph: &Vec<Vec<(usize, u32)>>, dest: &Vec<usize>) -> Vec<usize> {
    let mut hq = BinaryHeap::new();
    let mut distance = vec![u32::MAX; n + 1];
    distance[st] = 0;
    hq.push((Reverse(distance[st]), false, st));
    let mut used = vec![false; n + 1];

    while let Some((Reverse(dist), vis, cur)) = hq.pop() {
        if distance[cur] < dist {
            continue;
        }
        for &(nxt, cost) in &graph[cur] {
            let mut tmp = vis;
            if (cur == g && nxt == h) || (cur == h && nxt == g) {
                tmp = true;
            }
            if dist + cost < distance[nxt] {
                distance[nxt] = dist + cost;
                used[nxt] = tmp;
                hq.push((Reverse(distance[nxt]), tmp, nxt));
            } else if !used[nxt] && tmp && dist + cost == distance[nxt] {
                used[nxt] = tmp;
                hq.push((Reverse(distance[nxt]), tmp, nxt));
            }
        }
    }

    let mut res: Vec<usize> = dest.iter().cloned().filter(|&i| used[i]).collect();
    res.sort();
    res
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();
    let mut res = String::new();

    let t: usize = next().parse().unwrap();
    for _ in 0..t {
        let (n, m, k): (usize, usize, usize) = (next().parse().unwrap(), next().parse().unwrap(), next().parse().unwrap());
        let (s, g, h): (usize, usize, usize) = (next().parse().unwrap(), next().parse().unwrap(), next().parse().unwrap());
        let mut graph = vec![Vec::new(); n + 1];
        for _ in 0..m {
            let (u, v, w): (usize, usize, u32) = (next().parse().unwrap(), next().parse().unwrap(), next().parse().unwrap());
            graph[u].push((v, w));
            graph[v].push((u, w));
        }

        let mut dest = Vec::with_capacity(k);
        for _ in 0..k {
            let d: usize = next().parse().unwrap();
            dest.push(d);
        }

        let dist = dijkstra(s, n, g, h, &graph, &dest);
        for d in dist {
            res.push_str(d.to_string().as_str());
            res.push(' ');
        }
        res.push('\n');
    }

    print!("{res}")
}
