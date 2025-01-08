use std::collections::{HashMap, HashSet};
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let mut planet: Vec<Vec<u32>> = Vec::with_capacity(n);
    let mut res = 0;
    for _ in 0..n {
        let tmp: Vec<u32> = (0..m).map(|_| next().parse().unwrap()).collect();
        let tmp_set: HashSet<u32> = tmp.iter().map(|x| *x).collect();
        let mut tmp_list: Vec<u32> = tmp_set.iter().map(|x| *x).collect();
        tmp_list.sort();

        let tmp_map: HashMap<u32, u32> = tmp_list
            .iter()
            .cloned()
            .zip((0..tmp_list.len()).map(|x| x as u32))
            .collect();

        let new: Vec<u32> = tmp.iter().map(|x| *tmp_map.get(x).unwrap()).collect();

        res += planet.iter().filter(|x| **x == new).count();
        planet.push(new);
    }
    print!("{res}");
}
