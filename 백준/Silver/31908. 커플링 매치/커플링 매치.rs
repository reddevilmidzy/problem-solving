use std::collections::HashMap;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: u32 = next().parse().unwrap();
    let mut map: HashMap<&str, Vec<&str>> = HashMap::new();
    for _ in 0..n {
        let (per, ring): (&str, &str) = (next(), next());
        if ring == "-" {
            continue;
        }
        if !map.contains_key(&ring) {
            map.insert(ring, Vec::new());
        }
        map.get_mut(&ring).unwrap().push(per);
    }
    let mut res = String::new();
    let mut cnt = 0;
    for val in map.values() {
        if val.len() == 2 {
            writeln!(res, "{} {}", val[0], val[1]).unwrap();
            cnt += 1;
        }
    }
    println!("{cnt}");
    print!("{res}");
}
