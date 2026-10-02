# Data from swiggy_india.jsonl @ https://www.kaggle.com/datasets/archangel0x01/swiggy-india-restaurant-menu-data

import json
import pymysql

JSONL_FILE = 'data/swiggy_india.jsonl'

# Database connection configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'database': 'vendor_service_db',
    'charset': 'utf8mb4'
}

MAX_LINE_CNT = 40000 # The file has 182,295 lines


def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendors (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,

            name VARCHAR(255) NOT NULL,
            latitude DOUBLE NOT NULL,
            longitude DOUBLE NOT NULL,
            street_address VARCHAR(255) NOT NULL,
            area VARCHAR(255) NOT NULL,
            city VARCHAR(255) NOT NULL,
            avg_rating DECIMAL(3,2) NOT NULL DEFAULT 0.0
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            vendor_id BIGINT NOT NULL,

            name VARCHAR(255) NOT NULL,
            
            FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE CASCADE

        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            id BIGINT AUTO_INCREMENT PRIMARY KEY,
            vendor_id BIGINT NOT NULL,
            category_id BIGINT NOT NULL,

            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            description TEXT NOT NULL,

            FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE CASCADE,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        );
    """)

def seed_database():
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            create_tables(cursor)
            connection.commit()

            print(f"Streaming and seeding data from {JSONL_FILE}...")
            
            item_batch = []
            line_count = 0

            # Open file line by line (safe for memory)
            with open(JSONL_FILE, 'rt', encoding='utf-8') as f:
                for line in f:
                    if not line.strip():
                        continue
                    
                    try:
                        data = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    vendor_id = str(data.get('id'))
                    if not vendor_id:
                        continue


                    # Extract vendor fields according to your minimalist schema
                    city_info = data.get('city', {})
                    vendor_row = (
                        data.get('name'),
                        city_info.get('lat'),
                        city_info.get('lng'),
                        data.get('area'),       # street_address mapping
                        data.get('locality') or "",         # area mapping
                        city_info.get('name') or data.get('city_slug'),
                        data.get('avg_rating') or 0.0
                    )

                    # 1. Insert Vendor and get ID
                    vendor_query = """
                        INSERT INTO vendors (name, latitude, longitude, street_address, area, city, avg_rating)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """
                    # Execute vendor insert and grab vendor_id
                    cursor.execute(vendor_query, vendor_row)
                    vendor_id = cursor.lastrowid
                    # print(vendor_id)
                    # cnt = 0

                    # 2. Process Menu & Categories
                    menu = data.get("menu", [])
                    if isinstance(menu, list):
                        for category_data in menu:
                            category_name = category_data.get("category")
                            if not category_name:
                                continue

                             # Insert Category linked to this vendor and get category_id
                            category_query = """
                                    INSERT INTO categories (vendor_id, name)
                                    VALUES (%s, %s)
                                    ON DUPLICATE KEY UPDATE name = VALUES(name);
                            """
                            cursor.execute(category_query, (vendor_id, category_name))
                            category_id = cursor.lastrowid
                            
                            items = category_data.get('items', [])
                            item_batch = []
                            # print(f" Category {category_id}: {category_name} with {len(items)} items.")
                            # cnt += len(items)

                            if isinstance(items, list):
                                for item in items:
                                    if not item.get("name"):
                                        continue
                                    item_row = (
                                        vendor_id,
                                        category_id,
                                        item.get('name'),
                                        item.get('price'),
                                        item.get('description')
                                    )
                                    item_batch.append(item_row)
                                    # print(item.get('name'))

                                # 4. Batch Insert Items for this category using executemany
                                if item_batch:
                                    item_insert_query = """
                                                INSERT INTO menu_items (vendor_id, category_id, name, price, description)
                                                VALUES (%s, %s, %s, %s, %s);
                                            """
                                    cursor.executemany(item_insert_query, item_batch)

                    line_count += 1
                    if line_count % 1000 == 0:
                        print (f"Extracted line {line_count} successfully!")
                    # print (f"Extracted from {vendor_id}, {cnt} items!")

                    # Commit every 5000 lines
                    if line_count % 5000 == 0:
                        connection.commit()

                    if line_count > MAX_LINE_CNT:
                        print(f"Reached MAX_LINE_CNT ({MAX_LINE_CNT}). Stopping early.")
                        break
                    
                connection.commit()
                print("Seeding completed successfully!")

    except Exception as e:
        connection.rollback()
        print(f"An error occurred during seeding: {e}")
    finally:
        connection.close()

if __name__ == '__main__':
    seed_database()