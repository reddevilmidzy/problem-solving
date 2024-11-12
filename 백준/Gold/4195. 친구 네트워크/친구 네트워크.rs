use std::collections::HashMap;
use std::io::{self, BufRead};

fn find(parent: &mut HashMap<String, String>, x: &str) -> String {
    let parent_x = parent[x].clone();
    if parent_x != x {
        let root = find(parent, &parent_x);
        parent.insert(x.to_string(), root.clone());
        root
    } else {
        x.to_string()
    }
}

fn union(parent: &mut HashMap<String, String>, cnt: &mut HashMap<String, i32>, a: &str, b: &str) {
    let root_a = find(parent, a);
    let root_b = find(parent, b);
    if root_a != root_b {
        let pre_sum = cnt[&root_a] + cnt[&root_b];
        if root_a > root_b {
            parent.insert(root_a.clone(), root_b.clone());
            cnt.insert(root_b.clone(), pre_sum);
        } else {
            parent.insert(root_b.clone(), root_a.clone());
            cnt.insert(root_a.clone(), pre_sum);
        }
    }
}

fn main() {
    let stdin = io::stdin();
    let input = stdin.lock().lines();
    let mut iter = input.map(|line| line.unwrap());

    let t: usize = iter.next().unwrap().parse().unwrap();
    let mut sb = String::new();

    for _ in 0..t {
        let n: usize = iter.next().unwrap().parse().unwrap();
        let mut parent: HashMap<String, String> = HashMap::new();
        let mut cnt: HashMap<String, i32> = HashMap::new();

        for _ in 0..n {
            let line = iter.next().unwrap();
            let mut users = line.split_whitespace();
            let user1 = users.next().unwrap().to_string();
            let user2 = users.next().unwrap().to_string();

            if !parent.contains_key(&user1) {
                parent.insert(user1.clone(), user1.clone());
                cnt.insert(user1.clone(), 1);
            }
            if !parent.contains_key(&user2) {
                parent.insert(user2.clone(), user2.clone());
                cnt.insert(user2.clone(), 1);
            }
            union(&mut parent, &mut cnt, &user1, &user2);
            sb.push_str(&cnt[&find(&mut parent, &user1)].to_string());
            sb.push_str("\n");
        }
    }

    print!("{}", sb);
}