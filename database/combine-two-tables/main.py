""" 
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
personId is the primary key (column with unique values) for this table.
This table contains information about the ID of some persons and their first and last names.

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key (column with unique values) for this table.
Each row of this table contains information about the city and state of one person with ID = PersonId.

Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
Explanation: 
There is no address in the address table for the personId = 1 so we return null in their city and state.
addressId = 1 contains information about the address of personId = 2.
"""
def create_person_table():
    """Create and populate Person table"""
    person_data = [
        {'personId': 1, 'lastName': 'Wang', 'firstName': 'Allen'},
        {'personId': 2, 'lastName': 'Alice', 'firstName': 'Bob'}
    ]
    return person_data

def create_address_table():
    """Create and populate Address table"""

    address_data = [
        {'addressId': 1, 'personId': 2, 'city': 'New York City', 'state': 'New York'},
        {'addressId': 2, 'personId': 3, 'city': 'Leetcode', 'state': 'California'}  
    ]
    return address_data

def join_person_address(person_table, address_table):
    """Join person and address tables and return required fields"""

def combine_two_tables(person_table, address_table):
    # Create dictionaries to store person and address information
    person_dict = {person['personId']: person for person in person_table}
    address_dict = {address['personId']: address for address in address_table}

    # Combine person and address information
    result = []
    for person_id, person_info in person_dict.items():
        address_info = address_dict.get(person_id, {'city': None, 'state': None})
        result.append({
            'firstName': person_info['firstName'],
            'lastName': person_info['lastName'],
            'city': address_info['city'],
            'state': address_info['state']
        })

    return result