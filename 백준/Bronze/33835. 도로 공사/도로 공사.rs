use std::io::{read_to_string, stdin};

fn dist(st_y: i64, st_x: i64, ed_y: i64, ed_x: i64) -> f64 {
    (((st_y - ed_y).pow(2) + (st_x - ed_x).pow(2)) as f64).sqrt()
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut tmp = Vec::new();

    for i in 0..n {
        let (x, y): (i64, i64) = (next().parse().unwrap(), next().parse().unwrap());
        if i == 0 {
            tmp.push((x, y));
        }
        if i == n - 1 {
            tmp.push((x, y));
        }
    }

    print!("{}", dist(tmp[0].0, tmp[0].1, tmp[1].0, tmp[1].1));
}
