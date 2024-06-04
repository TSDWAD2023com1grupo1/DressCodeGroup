-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: dresscode_2
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add articulos carrito',7,'add_articuloscarrito'),(26,'Can change articulos carrito',7,'change_articuloscarrito'),(27,'Can delete articulos carrito',7,'delete_articuloscarrito'),(28,'Can view articulos carrito',7,'view_articuloscarrito'),(29,'Can add articulos pedido',8,'add_articulospedido'),(30,'Can change articulos pedido',8,'change_articulospedido'),(31,'Can delete articulos pedido',8,'delete_articulospedido'),(32,'Can view articulos pedido',8,'view_articulospedido'),(33,'Can add carritos',9,'add_carritos'),(34,'Can change carritos',9,'change_carritos'),(35,'Can delete carritos',9,'delete_carritos'),(36,'Can view carritos',9,'view_carritos'),(37,'Can add categorias',10,'add_categorias'),(38,'Can change categorias',10,'change_categorias'),(39,'Can delete categorias',10,'delete_categorias'),(40,'Can view categorias',10,'view_categorias'),(41,'Can add envios',11,'add_envios'),(42,'Can change envios',11,'change_envios'),(43,'Can delete envios',11,'delete_envios'),(44,'Can view envios',11,'view_envios'),(45,'Can add pagos',12,'add_pagos'),(46,'Can change pagos',12,'change_pagos'),(47,'Can delete pagos',12,'delete_pagos'),(48,'Can view pagos',12,'view_pagos'),(49,'Can add pedidos',13,'add_pedidos'),(50,'Can change pedidos',13,'change_pedidos'),(51,'Can delete pedidos',13,'delete_pedidos'),(52,'Can view pedidos',13,'view_pedidos'),(53,'Can add productos',14,'add_productos'),(54,'Can change productos',14,'change_productos'),(55,'Can delete productos',14,'delete_productos'),(56,'Can view productos',14,'view_productos'),(57,'Can add usuarios',15,'add_usuarios'),(58,'Can change usuarios',15,'change_usuarios'),(59,'Can delete usuarios',15,'delete_usuarios'),(60,'Can view usuarios',15,'view_usuarios');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-03 16:03:08
