-- ============================================
-- Supershop Management Database Schema
-- ============================================

-- Create Database
CREATE DATABASE IF NOT EXISTS supershopmanagement;
USE supershopmanagement;

-- ============================================
-- CUSTOMER TABLE
-- ============================================
CREATE TABLE IF NOT EXISTS Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ContactInfo VARCHAR(100),
    Address VARCHAR(200),
    MembershipStatus ENUM('Regular', 'Premium') DEFAULT 'Regular',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- PRODUCT TABLE
-- ============================================
CREATE TABLE IF NOT EXISTS Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Price DECIMAL(10,2) NOT NULL,
    QuantityInStock INT DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- EMPLOYEE TABLE
-- ============================================
CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Role VARCHAR(50),
    Salary DECIMAL(10,2),
    ContactInfo VARCHAR(100),
    Address VARCHAR(200),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- SUPPLIER TABLE
-- ============================================
CREATE TABLE IF NOT EXISTS Supplier (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ContactInfo VARCHAR(100),
    Address VARCHAR(200),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

