use std::collections::HashMap;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();

    let a: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();
    let b: Vec<u32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut cnt_a = HashMap::new();
    let mut cnt_b = HashMap::new();

    for &val in &a {
        *cnt_a.entry(val).or_insert(0) += 1;
    }
    for &val in &b {
        *cnt_b.entry(val).or_insert(0) += 1;
    }

    let mut max_match = 0;
    let mut match_a = Vec::new();
    let mut match_b = Vec::new();
    
    let mut not_a = Vec::new();
    let mut not_b = Vec::new();

    for (&val, &count_a) in &cnt_a {
        if let Some(&count_b) = cnt_b.get(&val) {
            let match_count = count_a.min(count_b);
            max_match += match_count;

            for _ in 0..match_count {
                match_a.push(val);
                match_b.push(val);
            }

            if count_a > match_count {
                for _ in 0..(count_a - match_count) {
                    not_a.push(val);
                }
            }
            if count_b > match_count {
                for _ in 0..(count_b - match_count) {
                    not_b.push(val);
                }
            }
        } else {
            for _ in 0..count_a {
                not_a.push(val);
            }
        }
    }

    for (&val, &count_b) in &cnt_b {
        if !cnt_a.contains_key(&val) {
            for _ in 0..count_b {
                not_b.push(val);
            }
        }
    }

    not_a.sort();
    not_b.sort();

    match_a.extend(not_a);
    match_b.extend(not_b);

    println!("{}", max_match);
    println!("{}", match_a.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" "));
    println!("{}", match_b.iter().map(|x| x.to_string()).collect::<Vec<_>>().join(" "));
}
