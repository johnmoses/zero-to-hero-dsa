// Database Fundamentals - Java example (SQLite with JDBC)

import java.sql.*;

public class Main {
    public static void main(String[] args) {
        String url = "jdbc:sqlite::memory:";

        try (Connection conn = DriverManager.getConnection(url)) {
            Statement stmt = conn.createStatement();
            stmt.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);");
            stmt.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25);");

            ResultSet rs = stmt.executeQuery("SELECT * FROM users;");
            while (rs.next()) {
                System.out.println(rs.getInt("id") + "\t" +
                                   rs.getString("name") + "\t" +
                                   rs.getInt("age"));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
