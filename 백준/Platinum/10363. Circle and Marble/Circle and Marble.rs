use std::collections::HashSet;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut res = String::new();

    let t: usize = next().parse().unwrap();
    for i in 1..=t {
        let n: usize = next().parse().unwrap();
        let cnt: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
        let par: Vec<usize> = (0..n).map(|_| next().parse().unwrap()).collect();
        writeln!(res, "Case #{i}: {}", solve(n, cnt, par)).unwrap();
    }
    print!("{res}");
}

fn mex(nums: Vec<i32>) -> i32 {
    for i in 0..nums.len() {
        if nums[i] != i as i32 {
            return i as i32;
        }
    }
    nums.len() as i32
}

fn get_grundy(graph: &Vec<Vec<usize>>, grundy: &mut Vec<i32>, cur: usize) -> i32 {
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
    let mut nums: Vec<i32> = nums.into_iter().collect();
    nums.sort();
    grundy[cur] = mex(nums);
    grundy[cur]
}

fn solve(n: usize, cnt: Vec<u32>, par: Vec<usize>) -> String {
    let mut graph = vec![Vec::new(); n];
    for i in 0..n {
        if par[i] == 0 {
            continue;
        }
        graph[par[i] - 1].push(i);
    }

    let mut res = 0;
    let mut grundy = vec![-1; n];
    for cur in 0..n {
        if cnt[cur] % 2 != 0 {
            res ^= get_grundy(&graph, &mut grundy, cur);
        }
    }

    if res != 0 {
        return "first".to_string();
    }
    "second".to_string()
}

#[test]
fn tmp() {
    // solve(3, vec![1, 1, 2], vec![0, 1, 2]);
    println!("{}", solve(4, vec![1, 1, 2, 3], vec![0, 1, 1, 3]));
}
