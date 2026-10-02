# Crave Drop 😋🍽️🛵

## Tech Stack and Tools 🧰🛠️
Java, Spring Boot Spring Framework, Redis, Maven, Apache Kafka, MySQL, Docker Compose

## Requirements 📋
| Functional                  | Non Functional    | 
| --------------------------- | ----------------- |
| Restaurant & Menu Browsing  | Scalability       |
| Order Placement             | High Availability |
| Driver Tracking             | Low Latency       |
| Driver Order Assignment     |                   |

## Data Model 🛢️
<img width="1622" height="885" alt="db" src="https://github.com/user-attachments/assets/8d22700d-5099-4b53-8996-19575e071e39" />

## Database Boundaries per Service 🚧
<img width="1622" height="899" alt="db" src="https://github.com/user-attachments/assets/3af410ea-1909-43bc-8ca5-3f93b0d66fe1" />


## Architecture 🏗️
<img width="2370" height="4496" alt="cravedrop_architecture" src="https://github.com/user-attachments/assets/5ade4b31-d01e-41b9-87b1-ee2363d724c7" />

## API Design
- Location Service 📍
    - POST   /locations/drivers/update
    - GET    /locations/driver/nearby
        - Params: Latitude, Longitude, Radius (optional)
    - DELETE /locations/drivers/{driverId}

##  🙏 Acknowledgements
- The foundational base for select domain modules (such as driver tracking and matching logic, with the tutorial's ride service adapted into an order service  for a food delivery context) was **inspired, sourced, and adapted** from Yeshendra Dhaker's's Uber Clone tutorial [Github](https://github.com/YeshendraDhaker/Uber-App) | [Video](https://www.youtube.com/watch?v=Cdx4DF9N8d8)
- This project uses the "Swiggy India Restaurant & Menu Data" dataset **sourced** from [Kaggle](https://www.kaggle.com/datasets/archangel0x01/swiggy-india-restaurant-menu-data) the **swiggy_india.jsonl** file, created by archangel0x01 . It is licensed under the CC BY-SA 4.0
