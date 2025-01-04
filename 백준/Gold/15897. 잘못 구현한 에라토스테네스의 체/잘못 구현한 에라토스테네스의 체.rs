use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let n: f64 = next().parse().unwrap();
    // 100000000
    // 1957511487
    // let n = 10_i64.pow(9);
    // 21877697534
    // let n = 10_i64.pow(9);
    // let n: f64 = 36f64;
    let mut res: i64 = 0;

    for i in 1..=n.sqrt().ceil() as i64 {
        res += (n / i as f64).ceil() as i64;
    }

    let mut cur = n.sqrt().ceil() + 1f64;

    while cur <= n {
        let tmp = (n / cur).ceil();

        if tmp == 1f64 {
            res += 1;
            break;
        }
        let nxt = (n / (tmp - 1f64)).floor();
        // println!("add = {} cur = {}, nxt ={}", ((nxt - cur) * tmp) as i64, cur, nxt);
        res += ((nxt - cur) * tmp) as i64;
        if cur == nxt {
            res += (n / cur).ceil() as i64;
            cur += 1f64;
        } else {
            cur = nxt;
        }
    }

    print!("{res}");
}
