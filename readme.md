# Crave Drop 😋🍽️🛵

## Tech Stack and Tools 🧰🛠️
Java, Spring Boot Spring Framework, Redis, Maven, Apache Kafka, MySQL, Docker Compose

## Requirements 📋
| Functional                  | Non Functional    | 
| --------------------------- | ----------------- |
| Restaurant & Menu Browsing  | Scalability       |
| Order Placement             | High Availability |
| Driver Tracking             | Low Latency
| Driver Order Assignment     |

## Data Model 🛢️
<img width="1527" height="843" alt="db" src="https://github.com/user-attachments/assets/38220e9a-d4f1-4b15-97bb-6fa07d26dd49" />

## Database Boundaries per Service 🚧
<img width="1528" height="844" alt="db" src="https://github.com/user-attachments/assets/974a2cde-0770-4243-9095-e6567c3a39ce" />

## Architecture 🏗️
<img width="2370" height="4496" alt="cravedrop_architecture" src="https://github.com/user-attachments/assets/5ade4b31-d01e-41b9-87b1-ee2363d724c7" />

## API Design
- Location Service 📍
    - POST   /locations/drivers/update
    - GET    /locations/driver/nearby
        - Params: Latitude, Longitude, Radius (optional)
    - DELETE /locations/drivers/{driverId}

##  🙏 Acknowledgements
- The foundational base for select domain modules (such as driver tracking and matching logic, with the tutorial's ride service adapted into an order service  for a food delivery context) was **inspired, sourced, and adapted** from Yeshendra Dhaker's's Uber Clone tutorial [Github](https://github.com/YeshendraDhaker/Uber-App) | [Video](https://www.youtube.com/watch?v=Cdx4DF9N8d8).
<img width="2370" height="4496" alt="cravedrop_architecture" src="https://github.com/user-attachments/assets/e2342c2e-47b1-4c9f-a360-9cfa01ccc838" />

