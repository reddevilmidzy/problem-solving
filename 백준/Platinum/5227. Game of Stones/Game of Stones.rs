use std::collections::HashSet;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut res = String::new();

    loop {
        let (n, m): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
        if n == 0 {
            break;
        }
        let mut graph = vec![Vec::new(); n];
        for _ in 0..m {
            let (u, v): (usize, usize) = (next().parse().unwrap(), next().parse().unwrap());
            graph[u].push(v);
        }
        let cnt: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
        writeln!(res, "{}", solve(n, graph, cnt)).unwrap();
    }

    print!("{res}");
}

fn mex(nums: Vec<i16>) -> i16 {
    for i in 0..nums.len() {
        if nums[i] != i as i16 {
            return i as i16;
        }
    }
    nums.len() as i16
}

fn get_grundy(graph: &Vec<Vec<usize>>, grundy: &mut Vec<i16>, cur: usize) -> i16 {
    if grundy[cur] != -1 {
        return grundy[cur];
    }
    let mut nums = HashSet::new();
    for &nxt in &graph[cur] {
        let val = if grundy[nxt] != -1 {
            grundy[nxt]
        } else {
            get_grundy(graph, grundy, nxt)
        };
        nums.insert(val);
    }
    let mut nums: Vec<i16> = nums.into_iter().collect();
    nums.sort();
    grundy[cur] = mex(nums);

    grundy[cur]
}

fn solve(n: usize, graph: Vec<Vec<usize>>, cnt: Vec<u32>) -> String {
    let mut res = 0;
    let mut grundy = vec![-1; n];
    for cur in 0..n {
        if cnt[cur] % 2 != 0 {
            res ^= get_grundy(&graph, &mut grundy, cur);
        }
    }
    if res != 0 {
        return "First".to_string();
    }
    "Second".to_string()
}
