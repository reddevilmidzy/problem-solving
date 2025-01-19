use std::collections::{HashSet, VecDeque};
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: u32 = next().parse().unwrap();
    let a: u32 = next().parse().unwrap();
    let b: u32 = next().parse().unwrap();

    let mut queue = VecDeque::new();
    queue.push_back((n, 0, false));
    let mut visited = HashSet::new();

    while let Some((cur, cnt, pre)) = queue.pop_front() {
        if cur == 0 {
            print!("{}", cnt + pre as i32);
            break;
        }

        if !pre && cur > a && !visited.contains(&(cur - a)) {
            visited.insert(cur - a);
            queue.push_back((cur - a, cnt, true));
        }
        if !pre && cur > b && !visited.contains(&(cur - b)) {
            visited.insert(cur - b);
            queue.push_back((cur - b, cnt, true));
        }
        if !visited.contains(&(cur - 1)) {
            visited.insert(cur - 1);
            queue.push_back((cur - 1, cnt + 1, false));
        }
    }
}
