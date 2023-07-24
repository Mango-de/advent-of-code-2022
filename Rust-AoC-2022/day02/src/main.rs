#![allow(non_snake_case)]

use std::collections::HashMap;
use std::fs::read_to_string;

fn main() {
    let lines = read_lines("../../../inputs/02");
    part1(&lines);
    part2(&lines);
}

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}

fn split_strings(lines: &Vec<String>) -> (Vec<&str>, Vec<&str>) {
    let mut va = Vec::new();
    let mut vb = Vec::new();

    for line in lines {
        if let [a, b] = line.split_whitespace().collect::<Vec<&str>>()[..] {
            va.push(a);
            vb.push(b);
        }
    }

    (va, vb)
}

fn solve(va: Vec<&str>, vb: Vec<&str>, scores: HashMap<&str, HashMap<&str, i32>>) -> i32 {
    let mut score = 0;

    for (&a, &b) in va.iter().zip(vb.iter()) {
        score += scores.get(a).unwrap().get(b).unwrap();
    }

    score
}

fn part1(lines: &Vec<String>) {
    let (va, vb) = split_strings(lines);

    let scores = HashMap::from([
        ("A", HashMap::from([("X", 4), ("Y", 8), ("Z", 3)])),
        ("B", HashMap::from([("X", 1), ("Y", 5), ("Z", 9)])),
        ("C", HashMap::from([("X", 7), ("Y", 2), ("Z", 6)])),
    ]);

    println!("{}", solve(va, vb, scores));
}

fn part2(lines: &Vec<String>) {
    let (va, vb) = split_strings(lines);

    let scores = HashMap::from([
        ("A", HashMap::from([("X", 3), ("Y", 4), ("Z", 8)])),
        ("B", HashMap::from([("X", 1), ("Y", 5), ("Z", 9)])),
        ("C", HashMap::from([("X", 2), ("Y", 6), ("Z", 7)])),
    ]);

    println!("{}", solve(va, vb, scores));
}
