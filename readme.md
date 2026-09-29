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
<img width="1503" height="888" alt="db" src="https://github.com/user-attachments/assets/8459e759-5792-45af-9114-d491667f3252" />

## Database Boundaries per Service 🚧
<img width="1513" height="911" alt="db" src="https://github.com/user-attachments/assets/fd1c8713-0ce6-4dbd-88b8-4ab0b81d4b21" />

## Architecture 🏗️
<img width="2370" height="4496" alt="cravedrop_architecture" src="https://github.com/user-attachments/assets/fdd3ffd1-9052-426a-8ca1-6533294b8b09" />

## API Design
- Location Service 📍
    - POST   /locations/drivers/update
    - GET    /locations/driver/nearby
        - Params: Latitude, Longitude, Radius (optional)
    - DELETE /locations/drivers/{driverId}

##  🙏 Acknowledgements
- The foundational base for select domain modules (such as driver tracking and matching logic, with the tutorial's ride service adapted into an order service  for a food delivery context) was **inspired, sourced, and adapted** from Yeshendra Dhaker's's Uber Clone tutorial [Github](https://github.com/YeshendraDhaker/Uber-App) | [Video](https://www.youtube.com/watch?v=Cdx4DF9N8d8).

