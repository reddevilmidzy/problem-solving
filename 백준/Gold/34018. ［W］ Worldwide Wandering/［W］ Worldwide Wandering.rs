use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

fn dijkstra(
    st: usize,
    n: usize,
    graph: &Vec<Vec<(usize, i64)>>,
    wait: &Vec<i64>,
) -> (Vec<i64>, Vec<i64>, Vec<i64>) {
    let inf = i64::MAX;
    let mut hq = BinaryHeap::new();
    let mut min_dist = vec![inf; n + 1];
    let mut max_dist = vec![-1; n + 1];

    min_dist[st] = 0;
    max_dist[st] = 0;

    let mut edge_cnt = vec![inf; n + 1];
    edge_cnt[st] = 0;
    hq.push(Reverse((edge_cnt[st], st)));

    while let Some(Reverse((cnt, cur))) = hq.pop() {
        if edge_cnt[cur] < cnt {
            continue;
        }

        for &(nxt, cost) in &graph[cur] {
            if cnt + 1 < edge_cnt[nxt] {
                edge_cnt[nxt] = cnt + 1;
                hq.push(Reverse((cnt + 1, nxt)));
 
                min_dist[nxt] = min_dist[nxt].min(min_dist[cur] + cost + wait[nxt]);
                max_dist[nxt] = max_dist[nxt].max(max_dist[cur] + cost + wait[nxt]);
            } else if cnt + 1 == edge_cnt[nxt] {
                min_dist[nxt] = min_dist[nxt].min(min_dist[cur] + cost + wait[nxt]);
                max_dist[nxt] = max_dist[nxt].max(max_dist[cur] + cost + wait[nxt]);
            }
        }
    }

    (edge_cnt, min_dist, max_dist)
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();

    let mut wait = vec![0; n + 1];

    for i in 2..=n {
        wait[i] = next().parse().unwrap();
    }

    let mut go = vec![Vec::new(); n + 1];
    let mut back = vec![Vec::new(); n + 1];

    for _ in 0..m {
        let (u, v, w): (usize, usize, i64) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );

        go[u].push((v, w));
        back[v].push((u, w));
    }

    let (go_cnt, go_min, go_max) = dijkstra(1, n, &go, &wait);
    let (back_cnt, back_min, back_max) = dijkstra(1, n, &back, &wait);

    let mut edge = i64::MAX;

    let mut min_res = i64::MAX;
    let mut max_res = i64::MIN;

    for cur in 2..=n {
        let tot_edge = go_cnt[cur] + back_cnt[cur];

        if edge < tot_edge {
        } else if edge == tot_edge {
            min_res = min_res.min(go_min[cur] + back_min[cur] - wait[cur]);
            max_res = max_res.max(go_max[cur] + back_max[cur] - wait[cur]);
        } else {
            edge = edge.min(tot_edge);
            min_res = go_min[cur] + back_min[cur] - wait[cur];
            max_res = go_max[cur] + back_max[cur] - wait[cur];
        }
    }

    print!("{}\n{}", min_res, max_res);
}
