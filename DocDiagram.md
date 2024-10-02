# HBnB Project – Technical Documentation

## 1. Introduction

This technical documentation presents the architecture and design of the HBnB project, a system for managing rental property listings similar to Airbnb. This document provides an overview of the application’s design by describing UML diagrams, API interaction flows, and the design decisions made. It will serve as a guide throughout the implementation phase, ensuring a clear reference for the development team.

The document is divided into several sections covering the high-level architecture, business logic, and API flows for managing listings, users, and interactions within the application.

## 2. High-Level Architecture

This section describes the overall architecture of the project using a three-layer model, with the application of **Facade Pattern** principles to facilitate interactions between the different layers.

The system is composed of three main layers:

- **User Interface**: This layer manages interactions with the user through a web or mobile interface.
- **Business Logic Layer**: It includes classes and services that handle core operations such as creating listings, managing users, and interactions with reviews.
- **Data Access Layer**: This layer interacts with the database and ensures data persistence.

The application uses the **Facade Pattern** to hide the complexity of the business logic and provide a simplified interface to the upper layer.

## 3. Business Logic Layer

The UML diagram above shows the business logic design with the following main classes:

- **Users**: This class manages system user information, including credentials, roles, and relationships with property listings.
- **Places**: It represents the properties or rental listings created by users, with detailed information such as geolocation, price, and availability.
- **Reviews**: This class handles reviews left by users on property listings. It is related to both the `Users` and `Places` classes.
- **Cities** and **Countries**: These classes help structure geographical data, associating each listing with a city and a country.
- **Amenities**: Manages available amenities for each listing (e.g., Wi-Fi, pool).

## 4. API Interaction Flow

In this section, we detail interactions between components through sequence diagrams. These diagrams show how API calls are processed from the user interface layer down to the business logic and database layers.

### Example API: Creating a Listing (Place)

1. The user sends a request to create a listing.
2. The request is validated by the user interface layer.
3. The business logic layer interacts with `Users`, `Places`, and `Amenities` classes to create and validate the listing.
4. Information is saved to the database.
5. A success or error response is sent back to the user.

(Insert sequence diagram for this example here)

## 5. Explanatory Notes

#### High-Level Architecture:
The package diagram clearly shows the separation of responsibilities between different layers. The **Facade Pattern** is used to centralize calls between the business logic and the database, making code maintenance easier.

#### Business Logic:
Each class is designed to represent a key entity in the HBnB system. The relationships between entities like `Places`, `Users`, and `Reviews` reflect real-world interactions in a property rental system.

#### API Interaction:
The APIs are designed to be simple and consistent, facilitating integration with front-end clients (e.g., a web or mobile application). Each API interaction has been optimized to minimize unnecessary database calls while ensuring robust checks at each step.

## 6. Conclusion

This documentation provides a comprehensive guide for implementing the HBnB project. It ensures that development and design teams share a clear understanding of the architecture and relationships between system components. By following this structure, the project can be developed in a modular way, allowing for future scalability.
