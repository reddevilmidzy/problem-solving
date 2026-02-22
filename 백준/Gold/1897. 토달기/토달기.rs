use std::collections::{HashSet, VecDeque};
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let d = next().parse::<u32>().unwrap();
    let st = next().parse::<String>().unwrap();
    let words = (0..d)
        .map(|_| next().parse::<String>().unwrap())
        .collect::<HashSet<_>>();

    let mut res = st.clone();
    let mut queue = VecDeque::new();
    let mut visited = HashSet::new();
    visited.insert(st.clone());
    queue.push_back(st);

    while let Some(cur) = queue.pop_front() {
        if res.len() < cur.len() {
            res = cur.clone();
        }
        for i in 0..=cur.len() {
            for j in 0..26 {
                let mut tmp = cur.clone();
                tmp.insert(i, ('a' as u8 + j) as char);
                if words.contains(&tmp) && visited.insert(tmp.clone()) {
                    queue.push_back(tmp);
                }
            }
        }
    }

    print!("{res}");
}
