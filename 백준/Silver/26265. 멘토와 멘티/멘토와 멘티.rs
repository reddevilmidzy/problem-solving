use std::collections::HashMap;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut res = String::new();

    let mut mentos: HashMap<&str, Vec<&str>> = HashMap::new();
    for _ in 0..n {
        let (u, v) = (next(), next());
        mentos.entry(u).or_insert_with(Vec::new).push(v);
    }

    let mut keys: Vec<&str> = mentos.clone().keys().map(|x| *x).collect();
    keys.sort();

    for key in keys {

        let mut menty = mentos.get_mut(key).unwrap();

        menty.sort();
        menty.reverse();

        for val in menty {
            writeln!(res, "{key} {val}").unwrap();
        }
    }
    print!("{res}");
}
