#![allow(non_snake_case)]

use std::fs::read_to_string;

fn main() {
    let lines = read_lines("../../../inputs/04");
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

fn format_lines(lines: &Vec<String>) -> Vec<((i32, i32), (i32, i32))> {
    lines
        .iter()
        .map(|line| {
            let tuples: Vec<&str> = line.split(',').collect();
            let first_tuple: Vec<i32> = tuples[0]
                .split('-')
                .map(|num| num.parse().expect("Invalid number format"))
                .collect();
            let second_tuple: Vec<i32> = tuples[1]
                .split('-')
                .map(|num| num.parse().expect("Invalid number format"))
                .collect();

            (
                (first_tuple[0], first_tuple[1]),
                (second_tuple[0], second_tuple[1]),
            )
        })
        .collect()
}

fn part1(lines: &Vec<String>) {
    let mut overlapping = 0;

    let formatted_lines = format_lines(lines);

    for (r1, r2) in formatted_lines {
        if (r1.0 <= r2.0 && r1.1 >= r2.1) || (r2.0 <= r1.0 && r2.1 >= r1.1) {
            overlapping += 1;
        }
    }

    println!("{}", overlapping);
}

fn part2(lines: &Vec<String>) {
    let mut overlapping = 0;

    let formatted_lines = format_lines(lines);

    for (r1, r2) in formatted_lines {
        if r2.0 <= r1.0 && r1.0 <= r2.1
            || r2.0 <= r1.1 && r1.1 <= r2.1
            || r1.0 <= r2.0 && r2.0 <= r1.1
            || r1.0 <= r2.1 && r2.1 <= r1.1
        {
            overlapping += 1;
        }
    }

    println!("{}", overlapping);
}
