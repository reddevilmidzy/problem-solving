use std::collections::HashMap;
use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut res = String::new();

    let t: u32 = next().parse().unwrap();
    for _ in 0..t {
        let s: String = next().parse().unwrap();
        let con: String = next().parse().unwrap();

        let mut score = HashMap::new();
        for c in s.split(",") {
            let mut kv = c.split(":").collect::<Vec<_>>();
            score.insert(kv[0], kv[1].parse::<i32>().unwrap());
        }

        let mut ans = i32::MAX;

        for c in con.split("|") {
            let mut tmp = 0;
            let mut c = c.split("&");

            while let Some(c) = c.next() {
                tmp = tmp.max(*score.get(c).unwrap());
            }

            ans = ans.min(tmp);
        }

        writeln!(res, "{ans}").unwrap();
    }

    print!("{res}");
}
