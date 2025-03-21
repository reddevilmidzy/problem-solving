use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let s = next();
    let mut cnt = 0;
    let mut res = 0;

    for i in s.chars() {
        if i == '1' {
            res = res.max((cnt + 1) / 2);
            cnt = 0;
        } else {
            cnt += 1;
        }
    }
    print!("{res}");
}
