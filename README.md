# old-town-jewels
# About
Old Town Jewels is an online jewellery store built using the Django web framework. It was developed as a part of a Fullstack course with Code Institute.

The store offers a wide variety of beautiful and unique jewellery pieces, including rings, earrings, necklaces, and more. Customers can browse the store's inventory, add items to their cart, and complete their purchase securely through the website.

Old Town Jewels is designed to be user-friendly and easy to navigate. The store features a clean and modern design, with high-quality product photos and detailed product descriptions to help customers make informed purchasing decisions.

Whether you're looking for a special piece of jewellery for yourself or a gift for someone else, Old Town Jewels has something for everyone. We hope you enjoy shopping with us!

![App Screenshot](static/images/am-i-responsive.png)

[View the live project here](https://old-town-jewels.herokuapp.com/ "Link to deployed site - Old Town Jewels")


# Table of Contents

[User Experience](#user-experience)

- [Strategy](#strategy)

- [User Stories](#user-stories)

- [Scope](#scope)

- [Structure](#structure)
    - [Design](#design)
        - [Wireframes](#wireframes)
        - [Color Schema](#color-schema)
        - [Model Schema](#model-schema)

[Marketing Strategies](#marketing-strategies)

[Features](#features)

[Features to be Implemented](#features-to-be-implemented)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Validator Testing](#validator-testing)

[Responsive Testing](#responsive-testing)

[Bugs Found](#bugs-found)

[User Feedback](#user-feedback)

[Search Engine Optimisation (SEO)](#search-engine-optimisation-seo)

[Deployment](#deployment)

[Credit](#credit)

[Acknowledgments](#Acknowledgments)


# User experience

At Old Town Jewels, our goal is to provide an enjoyable and seamless shopping experience for both our customers and the store owner. To achieve this, we have implemented the following strategies:

# Strategy
## For Customer
1. Easy navigation: We have designed the store's layout and menu to be intuitive and easy to use, so customers can easily find  what they are looking for.

2. Clear product descriptions: We have provided detailed descriptions of each product, including information on materials, sizing, and care instructions. This helps customers make informed purchasing decisions.

3. Secure checkout: We have implemented secure payment methods and encrypted data transmission to protect our customers' personal and financial information.

## For Owner 
1. Easy inventory management: We have provided tools for the owner to easily add, update, and delete products from the store's inventory.

2. Detailed sales reports: The owner can access reports on sales data, including total revenue.

By following these strategies, we hope to create a positive user experience for our customers and encourage them to shop with us again in the future.

# User Stories
As the superuser of Old Town Jewels, I want to be able to:

1. **Add and manage products**: I want to be able to easily add new products to the store's inventory, as well as update and delete existing products.

2. **View and analyze sales data**: I want to be able to access detailed reports on sales data, including total revenue and popular products.

3. **Manage user accounts**: I want to be able to add, update, and delete user accounts, including customer and employee accounts.

4. **Manage orders**: I want to be able to view and manage orders, including marking orders as shipped and canceling orders if necessary.

5. **Create and manage coupons**: I want to be able to create and manage coupons, including setting expiration dates and usage limits, and track their usage.

By being able to perform these tasks, I can effectively manage and maintain the Old Town Jewels store.

As a shopper at Old Town Jewels, I want to be able to:

1. **Easily browse and search for products**: I want to be able to easily browse through the store's inventory and use section filters to find specific products.

2. **View detailed product information**: I want to be able to see photos of the products and read detailed descriptions, including information on materials, sizing, and care instructions.

3. **Add items to my cart and complete my purchase**: I want to be able to easily add items to my cart and complete my purchase securely through the website.

4. **Apply coupons to my order**: I want to be able to enter a coupon code at checkout and have the discount applied to my order.

By being able to perform these tasks, I can easily shop and make purchases at Old Town Jewels.

# Scope

# User Story 1: Easily browse and search for products
Customers can easily browse through the store's inventory and use search filters to find specific products.

# User Story 2: View detailed product information
Customers can view high-quality photos of the products and read detailed descriptions, including information on materials, sizing, and care instructions.

# User Story 3: Add items to my cart and complete my purchase
Customers can easily add items to their cart and complete their purchase securely through the website.

# User Story 4: Apply coupons to my order
Customers have the option to apply coupons to their orders at checkout by entering a coupon code.

# Superuser

# User Story 5: Add and manage products
As the superuser of the store, I can easily add and manage products.

# User Story 6: View and analyze sales data
As the superuser of the store, I can view and analyze sales data, including total revenue and popular products.

# User Story 7: Manage user accounts
As the superuser of the store, I can manage user accounts, including customer and employee accounts. 

# User Story 8: View and analyze sales data
As the superuser of the store, I can access detailed reports on sales data, including total revenue and popular products.

# User Story 9: Manage user accounts
As the superuser of the store, I can add, update, and delete user accounts, .

# User Story 10: Manage orders
As the superuser of the store, I can view and manage orders, including marking orders as shipped and canceling orders if necessary.

# User Story 11: Create and manage coupons
As the superuser of the store, I can create and manage coupons, including setting expiration dates and usage limits, and track their usage.

By providing these features, Old Town Jewels aims to create a positive shopping experience for both customers and the store owner.


# Structure

This project is structured with a homepage with the website's logo and a message that greets the user with a clear navigation bar at the top of the page where the user can login or sign up. Old Town Jewels shop enables clients to browse products, add them to the cart, apply discount codes, go through the checkout process and pay with a credit a card.

**The website is made of the following apps**:

1. MyShop
2. Users
3. Cart
4. Coupons
5. Orders
6. Payment
7. Shop

## Design
The website was designed to be visually appealing and user-friendly, allowing for easy browsing and quick purchasing of desired items. To ensure an optimal layout, wireframes were created for various screen sizes including desktop, tablet, and mobile, and a limited color palette was utilized to maintain a cohesive appearance throughout the site.

- ## Wireframes
wireframes for the project were created using [Balsamiq](https://balsamiq.com/)

- ## Model Schema

Our application uses two different databases: SQLite for local development and Postgres for the deployed app on Heroku. SQLite is a lightweight, file-based database that is easy to set up and use for development purposes. Postgres is a more powerful and feature-rich relational database that is well suited for production environments.

For local development, we use SQLite as the database. SQLite is included in Python's standard library and requires no additional setup.

For the deployed app on Heroku, we use Postgres as the database. Postgres is a powerful, open-source relational database that is well suited for production environments. It offers robust data integrity and security features, as well as advanced performance and scalability.

We have created a separate data model for each of the databases, which defines the tables, fields, and relationships used in the application. The data model for SQLite is designed for local development and is optimized for ease of use and rapid development. The data model for Postgres is designed for production and is optimized for performance, scalability, and data integrity.

To set up the databases, you will need to install SQLite and Postgres on your local machine and configure the appropriate settings in the application's configuration file. Once the databases are set up, you can use any SQL client to interact with the databases, such as the SQLite command-line tool or pgAdmin for Postgres.

Keep in mind that SQLite is file-based while Postgres is server-based, so you will have to configure the appropriate settings in the application's configuration file to connect the app to the right database depending on the environment, local or production.

Please note that the SQLite database will be created automatically when you run the application for the first time in local environment and the Postgres database should be created manually in Heroku before you deploy your app.

