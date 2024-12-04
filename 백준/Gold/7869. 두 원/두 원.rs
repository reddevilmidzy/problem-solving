use std::f64::consts::PI;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let x1: f64 = next().parse().unwrap();
    let y1: f64 = next().parse().unwrap();
    let r1: f64 = next().parse().unwrap();

    let x2: f64 = next().parse().unwrap();
    let y2: f64 = next().parse().unwrap();
    let r2: f64 = next().parse().unwrap();

    let dist: f64 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)).sqrt();

    if r1 + r2 <= dist { // 안겹침
        print!("0.000");
    } else if (r1 - r2).abs() >= dist { // 큰원에 먹힘
        print!("{:.3}", r1.min(r2) * r1.min(r2) * PI);
    } else {
        let theta1 = ((r1 * r1 + dist * dist - r2 * r2) / (2.0 * r1 * dist)).acos();
        let theta2 = ((r2 * r2 + dist * dist - r1 * r1) / (2.0 * r2 * dist)).acos();
        // println!("{}, {}", theta1, theta2);
        print!("{:.3}", (r1 * r1 * theta1) - (r1 * r1 * (2.0 * theta1).sin() / 2.0) + (r2 * r2 * theta2) - (r2 * r2 * (2.0 * theta2).sin() / 2.0));
    }
}
