use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn count(y: i32, x: i32, visited: &Vec<Vec<bool>>, n: i32) -> i32 {
    let mut res = 0;
    for (dy, dx) in [
        (-1, 2),
        (-1, -2),
        (1, 2),
        (1, -2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
    ] {
        let ny = y + dy;
        let nx = x + dx;
        if ny < 0 || nx < 0 || ny >= n || nx >= n {
            continue;
        }
        let ny = ny as usize;
        let nx = nx as usize;

        if !visited[ny][nx] {
            res += 1;
        }
    }
    res
}

fn dist(n: i32, ed_y: i32, ed_x: i32) -> i32 {
    let st_y = n / 2;
    let st_x = n / 2;
    (st_y - ed_y).pow(2) + (st_x - ed_x).pow(2)
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();
    let mut stdout = String::new();

    let n: usize = next().parse().unwrap();
    let mut y: i32 = next().parse().unwrap();
    let mut x: i32 = next().parse().unwrap();
    y -= 1;
    x -= 1;

    let mut visited = vec![vec![false; n]; n];
    let n = n as i32;

    for _ in 0..n * n {
        visited[y as usize][x as usize] = true;
        writeln!(stdout, "{} {}", y + 1, x + 1).unwrap();

        let mut candy = Vec::new();
        for (dy, dx) in [
            (-1, 2),
            (-1, -2),
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ] {
            let ny = y + dy;
            let nx = x + dx;

            if ny < 0 || nx < 0 || ny >= n || nx >= n {
                continue;
            }
            if visited[ny as usize][nx as usize] {
                continue;
            }
            let cnt = count(ny, nx, &visited, n);
            let dist = dist(n, ny, nx);
            candy.push((cnt, -dist, ny, nx));
        }
        candy.sort_unstable();

        if !candy.is_empty() {
            y = candy[0].2;
            x = candy[0].3;
        }
        // println!("{y}, {x}, {:?}", candy);
    }

    let all = visited.iter().all(|row| row.iter().all(|&x| x));
    // print!("{all}");
    if all {
        print!("{stdout}");
    } else {
        print!("-1 -1");
    }
    // println!("{:?}", visited);
}
