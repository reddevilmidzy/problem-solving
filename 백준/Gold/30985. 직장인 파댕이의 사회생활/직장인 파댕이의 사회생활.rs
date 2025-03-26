use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

fn dijkstra(n: usize, st: usize, graph: &Vec<Vec<(usize, i64)>>) -> Vec<i64> {
    let inf = i64::MAX;
    let mut hq = BinaryHeap::new();
    let mut distance = vec![inf; n];

    distance[st] = 0;
    hq.push(Reverse((distance[st], st)));

    while let Some(Reverse((dist, cur))) = hq.pop() {
        if distance[cur] < dist {
            continue;
        }
        for &(nxt, cost) in &graph[cur] {
            if distance[cur] + cost < distance[nxt] {
                distance[nxt] = distance[cur] + cost;
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
    let k: usize = next().parse().unwrap();

    let mut graph = vec![Vec::new(); n];

    // 그냥 n개 복도까지 가는 시간 구한뒤. 엘베 시간 구하기
    for _ in 0..m {
        let (u, v, w): (usize, usize, i64) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );
        graph[u - 1].push((v - 1, w));
        graph[v - 1].push((u - 1, w));
    }

    let elv: Vec<i64> = (0..n).map(|_| next().parse().unwrap()).collect();

    let go = dijkstra(n, 0, &graph);
    let back = dijkstra(n, n - 1, &graph);

    let mut res = i64::MAX;

    // println!("{:?}", go);
    // println!("{:?}", back);

    for i in 0..n {
        if elv[i] == -1 {
            continue;
        }
        if go[i] == i64::MAX || back[i] == i64::MAX {
            continue;
        }
        let diff = (k - 1) as i64 * elv[i];
        res = res.min(go[i] + back[i] + diff);
    }
    if res == i64::MAX {
        res = -1;
    }
    print!("{res}");
}
