# Project Statement - AutoCrash Test

## Problem Statement

A driver may be unable to stop a vehicle before an obstacle because the vehicle continues moving during the driver's reaction time and then needs additional distance to brake. A simple program can combine these factors to estimate whether the vehicle stops before the obstacle and, when a crash occurs, estimate the speed and simplified person-impact quantities.

## Scope of the Project

The project accepts basic vehicle, brake and obstacle information. It calculates reaction distance, braking distance, total stopping distance and stopping time. When stopping is not possible before the obstacle, it calculates approximate impact speed and performs a simple person-impact analysis using kinetic energy and average impact force.

The project is an educational simulation and does not model real vehicle safety systems, road conditions, tyres, air resistance, vehicle deformation, seat belts, airbags or medical injury outcomes.

## Target Users

The project is intended for students and beginners who want to understand how basic Python programming concepts can be applied to a real-world physics-based problem.

## High-Level Features

- Vehicle and driver input
- Brake-type selection
- Speed conversion from km/h to m/s
- Reaction-distance calculation
- Braking-distance calculation
- Total stopping-distance and stopping-time calculation
- SAFE/CRASH decision
- Approximate impact-speed calculation
- Person kinetic-energy calculation
- Approximate average impact-force calculation
- Simple impact-speed classification
- Basic input validation
- Basic automated calculation tests
