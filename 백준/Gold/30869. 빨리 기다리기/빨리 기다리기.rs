use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();

    let mut graph = vec![Vec::new(); n + 1];
    for _ in 0..m {
        let (s, e, t, g): (usize, usize, i32, i32) = (
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
            next().parse().unwrap(),
        );
        graph[s].push((e, t, g));
    }

    print!("{}", dijkstra(n, k, 1, graph));
}

fn dijkstra(n: usize, k: usize, st: usize, graph: Vec<Vec<(usize, i32, i32)>>) -> i32 {
    let inf = i32::MAX;
    let mut distance = vec![vec![inf; n + 1]; k + 1];

    let mut hq = BinaryHeap::new();
    // hq 에 넣어야 하는 값은 현재까지 걸린 시간, 바꾼 횟수, 현재 위치,

    distance[0][st] = 0;
    hq.push((Reverse(distance[0][st]), 0, st));

    while let Some((dist, cnt, cur)) = hq.pop() {
        if distance[cnt][cur] < dist.0 {
            continue;
        }

        for &(nxt, cost, per) in &graph[cur] {
            // 웨잇
            let wait = if dist.0 % per == 0 {
                0
            } else {
                per - ((dist.0) % per)
            };
            if distance[cnt][cur] + cost + wait < distance[cnt][nxt] {
                distance[cnt][nxt] = distance[cnt][cur] + cost + wait;
                hq.push((Reverse(distance[cnt][nxt]), cnt, nxt));
            }
            if wait == 0 {
                continue;
            }
            // 여긴 대기 시간 추가 안해도 됨
            if cnt + 1 <= k && distance[cnt][cur] + cost < distance[cnt + 1][nxt] {
                distance[cnt + 1][nxt] = distance[cnt][cur] + cost;
                hq.push((Reverse(distance[cnt + 1][nxt]), cnt + 1, nxt));
            }
        }
    }

    let mut res = inf;
    for i in 0..=k {
        if distance[i][n] != inf {
            res = res.min(distance[i][n])
        }
    }

    if res != inf {
        res
    } else {
        -1
    }
}
